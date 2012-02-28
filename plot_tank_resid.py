import xija
from pylab import *
from Ska.Matplotlib import pointpair

start = '2011:001'
stop = '2011:180'
start = '2010:001'
stop = '2011:345'
start = '2011:180'
stop = '2012:056'

if 'model' not in globals():
    model = xija.ThermalModel('pftank2t', start=start, stop=stop,
                              model_spec='pftank2t/pftank2t_model_spec.json')
                              # model_spec='dpa/dpa_state_mask_lin_prop.json')
                              #model_spec='dpa/dpa_mask_clip.json')
                              #model_spec='dpa/dpa_prop.json')
    model.make()
    model.calc()

C2F = 1.8
dpa = model.get_comp('pftank2t')
xscatter = np.random.uniform(-0.2, 0.2, size=len(dpa.dvals)) * C2F
yscatter = np.random.uniform(-0.2, 0.2, size=len(dpa.dvals)) * C2F
clf()
resid = (dpa.dvals - dpa.mvals) * C2F
dvals = C2F * dpa.dvals + 32.0
plot(dvals + xscatter, resid + yscatter, '.', ms=1.0, alpha=1)
xlabel('PFTANK2T telemetry (degF)')
ylabel('Data - Model (degF)')
title('Residual vs. Data ({} - {})'.format(start, stop))

bins = np.arange(72, 102, 4.0)
r1 = []
r99 = []
ns = []
xs = []
for x0, x1 in zip(bins[:-1], bins[1:]):
    ok = (dvals >= x0) & (dvals < x1)
    residok = resid[ok]
    residok.sort()
    n = len(residok)
    i1 = int(0.01 * n)
    i99 = int(0.99 * n)
    xs.append((x0 + x1) / 2)
    r1.append(residok[i1])
    r99.append(residok[i99])
    ns.append(n)

xspp = pointpair(bins[:-1], bins[1:])
r1pp = pointpair(r1)
r99pp = pointpair(r99)

plot(xspp, r1pp, '-r')
plot(xspp, r99pp, '-r', label='1% and 99% limits')
grid()
ylim(-6.5, 10)
xlim(70, 102)

plot([70, 102], [3.0, 3.0], 'g--', alpha=1, label='+/- 3.0 degF')
plot([70, 102], [-3.0, -3.0], 'g--', alpha=1)
for x, n, y in zip(xs, ns, r99):
    text(x, max(y + 1, 5), 'N={}'.format(n),
         rotation='vertical', va='bottom', ha='center')

legend(loc='upper right')

# savefig('dpa_prop_resid_{}_{}.png'.format(start, stop))
# savefig('dpa_resid_{}_{}.png'.format(start, stop))
