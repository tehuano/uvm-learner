#!/usr/bin/python2.7
import os 
import sys

"""
high level support for doing this and that.
"""
def run(path):
    """
    high level support for doing this and that.
    """
    result = False
    filename = path + '/' + path + '.py'
    directory, module_name = os.path.split(filename)
    module_name = os.path.splitext(module_name)[0]

    path = list(sys.path)
    sys.path.insert(0, directory)
    try:
        module = __import__(module_name)
        result = module.run_test()
    finally:
        sys.path[:] = path # restore
    return result

if __name__ == '__main__':
    print("In main")
    #run('test')
