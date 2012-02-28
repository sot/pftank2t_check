"""Create the pftank2t model specification."""

# NOTE, this might not work since in the actual creation of
# pftank2t_model_spec.json some hand-edits were done along the way.  Hopefully
# this is not needed going forward.

import xija

P_pitches=[45, 60, 90, 120, 145, 180]
Ps =  [0.00695,
       -0.0958,
       -0.1273,
       -0.0816,
       0.04560,
       0.08471
       ]

mdl = xija.ThermalModel('pftank2t', start='2010:001', stop='2010:010')
pftank2t = mdl.add(xija.Node, 'pftank2t')
pf0tank2t = mdl.add(xija.Node, 'pf0tank2t')
pitch = mdl.add(xija.Pitch)
eclipse = mdl.add(xija.Eclipse)

mdl.add(xija.HeatSink, pf0tank2t, T=-100.0, tau=492.0)
mdl.add(xija.PropHeater, pf0tank2t, k=1.0, T_set=22.9)
mdl.add(xija.SolarHeat, pf0tank2t, pitch, eclipse, P_pitches, Ps, ampl=0.0038)
mdl.add(xija.Coupling, pftank2t, node2=pf0tank2t, tau=100.0)

mdl.make()
mdl.calc()
mdl.write('pftank2t.json')
# plot(mdl.times - mdl.times[0], mdl.comp['pftank2t'].mvals)

mvals = mdl.comp['pftank2t'].mvals
