# 1. The runProc variable is a subprocess.Popen object that runs the code.py file.
# 2. The communicate method is used to pass the input.txt file to the code.py file.
# 3. The input.txt file is read and passed to the code.py file.
# 4. The output of the code.py file is stored in the grep_stdout variable.
# 5. The grep_stdout variable is decoded using the latin-1 encoding.
# 6. The output is printed to the console.
# 7. The output.txt file is opened in write mode and the output is written to it.
# 8. The output.txt file is compared with the dest.txt file.
# 9. The time taken to run the code is printed.
#!/usr/bin/env python
# -*- coding: latin-1 -*-
# This function is used to run the code.py file.
# 
# :param: None
# :return: None

import os
import time
import subprocess
import compare


compileTimeout =10
runTimeout = 10
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
    print(grep_stderr.decode("latin-1"))
    # print(grep_stderr.decode('utf-8').rstrip('\r|\n'))
    pass
else:
    # print stdout
    # print(grep_stdout.decode('utf-8').rstrip('\r|\n'))

    # write output
    with open("output.txt", 'w', encoding='latin-1', newline='\n') as f:
        f.write(grep_stdout.decode("latin-1"))
        # f.write(grep_stdout.decode('utf-8').rstrip('\r|\n'))
    compare.compareFile('output.txt', 'dest.txt')

print("RUN TIME: ", (time.time()-t))
