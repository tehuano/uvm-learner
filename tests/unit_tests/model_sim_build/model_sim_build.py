#!/usr/bin/python2.7

import subprocess
import os
import sys
import re

test_model_path = os.path.dirname(os.path.realpath(__file__)) + '/../../test_model'
print("path: %s" % os.path.dirname(os.path.realpath(__file__)))

def run(cmd):
    print(cmd)
    os.system(cmd)

def check_output(string):
    #print(string)
    # vlog out example = Errors: 0, Warnings: 6
    result = re.search(r'Errors: [0-9]+', string).group().split()
    is_ok = (int(result[1]) == 0)
    return is_ok

def run_test():
    test_model_real_path = os.path.realpath(test_model_path)
    current_real_path = os.path.realpath('./')
    
    cmd = 'cd ' + test_model_real_path
    cmd = cmd + ';' + 'LD_LIBRARY_PATH=/lib32/ && make build'
    cmd = cmd + ';' + 'cd ' + current_real_path
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    #print(output)
    #print("Error: %s" % err)
    result = check_output(output)
    return result

if __name__ == "__main__":
    result = run_test()
    sys.exit(result)
    
