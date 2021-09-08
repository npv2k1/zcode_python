#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os
import time
import subprocess
import compare


compileTimeout = 5
runTimeout = 5
# format input and dest
compare.formatInput('input.txt')
compare.formatInput('dest.txt')

runProc = subprocess.Popen(
    args=['python', 'code.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE
)


(grep_stdout, grep_stderr) = runProc.communicate(
    input=open('input.txt', 'rb').read(), timeout=runTimeout)

t = time.time()

if(grep_stderr != b''):
    # print error
    # print(grep_stderr.decode("latin-1"))
    print(grep_stderr.decode('utf-8').rstrip('\r|\n'))
    pass
else:
    # print stdout
    # print(grep_stdout.decode('utf-8').rstrip('\r|\n'))

    # write output
    with open("output.txt", 'w', encoding='utf-8', newline='\n') as f:
        # f.write(grep_stdout.decode("latin-1"))
        f.write(grep_stdout.decode('utf-8').rstrip('\r|\n'))
    compare.compareFile('output.txt', 'dest.txt')

print("RUN TIME: ", (time.time()-t))
