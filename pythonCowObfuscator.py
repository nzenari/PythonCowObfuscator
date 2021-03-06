import dead_code
import generate_equivalent_instructions_sequence as gen
import obfuscate_variable as ov
import obfuscate_function as of
import replace_constants as rc
import sys
import getopt
import os


__author__ = "Ceoletta Valentina, Zanotti Mattia, Zenari Nicolo"
__version__ = '1.0'
__email__ = "{valentina.ceoletta, mattia.zanotti, nicolo.zenari}@studenti.univr.it"


def main(argv):

    if len(argv) == 0:
        print('Error: invalid use.')
        print('python3.6 pythonCowObfuscator.py -s <source.py>')
        sys.exit(2)

    try:
        opt, arg = getopt.getopt(argv, "s", ["idir="])
    except getopt.GetoptError:
        print('Error: invalid use.')
        print('python3.6 pythonCowObfuscator.py -s <source.py>')
        sys.exit(2)

    source = arg[0]

    # create dir result if not exists
    if not os.path.exists('result'):
        os.makedirs('result')

    # 1) dead code
    dead_code.start(source)

    # 2) gen sequence
    source = './result/output.py'
    with open('./result/result1.py', 'w') as res:
        for line in gen.replace_instructions(source):
            res.write(line)

    # 3) replace constants
    source = './result/result1.py'
    with open('./result/result2.py', 'w') as res:
        for line in rc.replace_constants(source):
            res.write(line)
    # 4) replace variables
    source = './result/result2.py'
    with open('./result/result3.py', 'w') as res:
        lines,dic = ov.obfuscate(source)
        for line in lines:
            res.write(line)

    # 5) replace function
    source = './result/result3.py'
    with open('./result/obfuscated.py', 'w') as res:
        for line in of.obfuscate(source, dic):
            res.write(line)


if __name__ == '__main__':
    main(sys.argv[1:])
