#!/usr/bin/python2.7
import os
import sys
import argparse
import inspect
sys.path.append('./unit_tests')
import TestUVM

# Create the parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')

# Add the arguments
my_parser.add_argument('-l',
                       '--list',
                       action='store_true',
                       help='list all the tests')
my_parser.add_argument('-r',
                       '--run',
                       type=str,
                       nargs='+',
                       help='run specific test')

def run(cmd):
    print(cmd)
    os.system(cmd)

if __name__ == '__main__':
    test = 'python2.7 -m unittest'

    # Execute parse_args()
    args = my_parser.parse_args()

    if args.list:
        print(inspect.getmembers(TestUVM.TestUVM, predicate=inspect.ismethod))
    elif args.run:  # Simplified long listing
        tests = ''
        for x in args.run:
            tests = tests + ' TestUVM.TestUVM.' + x
        test = test + tests
        cmd = 'cd unit_tests; {}; cd -'.format(test)
        run(cmd)
    else:
        cmd = 'cd unit_tests; {} TestUVM.TestUVM; cd -'.format(test)
        run(cmd)
    
