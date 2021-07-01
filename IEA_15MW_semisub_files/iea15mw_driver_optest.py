import os

from wisdem import run_wisdem

## File management
mydir = os.path.dirname(os.path.realpath(__file__))  # get path to this file
fname_wt_input = mydir + os.sep + "IEA-15-240-RWT_VolturnUS-S_optest.yaml"
fname_modeling_options = mydir + os.sep + "modeling_options_optest.yaml"
fname_analysis_options = mydir + os.sep + "analysis_options_optest_copy.yaml"

wt_opt, analysis_options, opt_options = run_wisdem(fname_wt_input, fname_modeling_options, fname_analysis_options)
