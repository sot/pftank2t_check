.. pftank2t documentation master file, created by

Chandra PFTANK2T model tools
==================================

This suite of tools provides the tools to use and maintain the Chandra 
PFTANK2T model.  The key elements are:

  - ``pftank2t_check.py``: Thermal check of command loads and validate PFTANK2T 
    model against recent telemetry

The PFTANK2T tools depend on Sybase tables and in particular the commanded states database
which is accessed primarily via the Chandra.cmd_states_ module.

.. _Chandra.cmd_states: ../pydocs/Chandra.cmd_states.html

pftank2t_check
========================

Overview
-----------

This code generates backstop load review outputs for checking the PFTANK2T
temperature.  It also generates PFTANK2T model validation plots comparing
predicted values to telemetry for the previous three weeks.

Command line options
---------------------

Typical use case
^^^^^^^^^^^^^^^^^

In the typical use case for doing load review the ``pftank2t_check`` tool will
propagate forward from a 5-minute average of the last available telemetry using
the ``cmd_states`` table.  The following options control the runtime behavior
of ``pftank2t_check``.

========================= ================================== ========================
Option                    Description                        Default           
========================= ================================== ========================
  --outdir=OUTDIR         Output directory                   out
  --oflsdir=OFLSDIR       Load products OFLS directory       None
  --model-spec=MODEL_SPEC PFTANK2T model specification file  pftank2t_model_spec.json
  --days=DAYS             Days of validation data (days)     100
  --run-start=RUN_START   Start time for regression testing  None
  --traceback=TRACEBACK   Enable tracebacks                  True
  --verbose=VERBOSE       Verbosity 0=quiet 1=normal 2=debug 1 (normal)
  --version               Print version                      
========================= ================================== ========================

Custom initial conditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the event that the Ska database is unavailable or specific
initial conditions are desired, the following options are provided.  The
only required option in this case is ``--T-pftank2t``.  All the rest have
default values that will produce a conservative (hot) prediction.

*NOTE: Specifying custom conditions STILL REQUIRES the Ska database in the current release.*

========================= ================================== ===================
Option                    Description                        Default           
========================= ================================== ===================
  --T-pftank2t=T_PFTANK2T Initial PFTANK2T value (degC)      None
  --pitch=PITCH           Initial pitch (degrees)            150
========================= ================================== ===================

Usage
--------

The typical way to use the ``pftank2t_check`` load review tool is via the script
launcher ``/proj/sot/ska/bin/pftank2t_check``.  This script sets up the Ska runtime
environment to ensure access to the correct python libraries.  This must be run
on a 64-bit linux machine.

::

  /proj/sot/ska/bin/pftank2t_check --oflsdir=/data/mpcrit1/mplogs/2009/MAY1809/oflsb \
                              --outdir=out 
  
  /proj/sot/ska/bin/pftank2t_check --oflsdir=/data/mpcrit1/mplogs/2009/MAY1809/oflsb \
                              --pitch=130.0 --T-pftank2t=45 --run-start 2009:137

  /proj/sot/ska/bin/pftank2t_check --outdir=regress2010 --run-start=2010:365 --days=360
 
