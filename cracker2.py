import itertools
import hashlib
import time
from joblib import Parallel, delayed
import multiprocessing

cracked = False

for oneLine in [line.rstrip('\n') for line in open('test.txt')]:
    start_time = time.time()
    cracked = False
    for x in range(1, 9):
        if cracked:
            break
        for p in itertools.product("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~", repeat = x):
            if cracked:
                break
            if hashlib.md5(''.join(p).encode('utf-8')).hexdigest() == oneLine:
                print 'Password for ' + oneLine + ' is ' + ''.join(p) + " and time spent is " + str(time.time() - start_time) + " seconds"
                cracked = True
                break
