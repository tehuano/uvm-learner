MSIM_PATH = /opt/intelFPGA/19.1/modelsim_ase/bin
UVM_PATH = /opt/intelFPGA/19.1/modelsim_ase/uvm-1.2/src
#$ ${MSIM_PATH}/vsim +UVM_TR_RECORD +UVM_VERBOSITY=HIGH +UVM_TESTNAME=simple_test

sim: clean
	g++ -c external.cpp -o external.o
	${MSIM_PATH}/vlog -work work -sv -stats=none ${UVM_PATH}/uvm_pkg.sv +incdir+${UVM_PATH}
clean:
	rm -rf DVEfiles csrc simv simv.daidir ucli.key .vlogansetup.args .vlogansetup.env .vcs_lib_lock simv.vdb AN.DB vc_hdrs.h *.diag *.vpd *tar.gz external.o

view_waves:
	dve &
