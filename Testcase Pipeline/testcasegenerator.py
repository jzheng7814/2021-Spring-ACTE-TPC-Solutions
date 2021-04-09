from string import ascii_letters, ascii_uppercase
from random import randint, choice
from itertools import combinations
from os import system
from math import ceil

prevusedrands = set()

def randstring():
    global prevusedrands

    string = ''.join([choice(ascii_letters) for i in range(randint(1, 50))])
    while string in prevusedrands:
        string = ''.join([choice(ascii_letters) for i in range(randint(1, 50))])
    prevusedrands.add(string)
    return string

with open('testcases.txt', 'w') as outfile:
    outfile.write("""sample testcase""")
    count = 0

    while count != 5:
        N = randint(1, 500)

        with open('in.txt', 'w') as testfile:
            def writestr(s):
                outfile.write(f'{s}\n')
                testfile.write(f'{s}\n')

            """write testcase and input into in stream and testcase.txt"""

        system('python3 "program path" > out.txt < in.txt')

        with open('out.txt', 'r') as infile:
            answer = infile.read()
        
        outfile.write(f'\n{answer}\n\n')
        count += 1
        