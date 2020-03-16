MODELSIM_PATH=/opt/intelFPGA/19.1/modelsim_ase/bin
UVM_PATH=/opt/intelFPGA/19.1/modelsim_ase/uvm-1.2/src

all: clean
	g++ -c external.cpp -o external.o
	${MODELSIM_PATH}/vlog -sv +incdir+{UVM_PATH} ${UVM_PATH}/uvm_pkg.sv top.sv external.o
clean:
	rm -rf DVEfiles csrc simv simv.daidir ucli.key .vlogansetup.args .vlogansetup.env .vcs_lib_lock simv.vdb AN.DB vc_hdrs.h *.diag *.vpd *tar.gz external.o

#view_waves:
#	dve &
