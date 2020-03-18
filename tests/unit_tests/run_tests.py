#!/usr/bin/python

import os
import platform

op_sys = platform.system()

modelsim_path = './'
test_script = 'xwz'

print(op_sys)
if 'Linux' == op_sys:
    modelsim_path = '/opt/intelFPGA/19.1/modelsim_ase/bin/'

def run(cmd):
    print(cmd)
    os.system(cmd)

cmd = modelsim_path + 'vlog' + ' -do ' + test_script
print(cmd)

#+ os.path.dirname(os.path.abspath(test_script).replace('\\', '/')) + '/}"' + ' -do "do ' +  + '"'
#run(cmd)
