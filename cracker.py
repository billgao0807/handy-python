import itertools
import hashlib
import time
from joblib import Parallel, delayed
import multiprocessing


def crack(oneLine):
    start_time = time.time()
    for x in range(1, 9):
        for p in itertools.product("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~", repeat = x):
            if hashlib.md5(''.join(p).encode('utf-8')).hexdigest() == oneLine:
                print 'Password for ' + oneLine + ' is ' + ''.join(p) + " and time spent is " + str(time.time() - start_time) + " seconds"
                return

num_cores = multiprocessing.cpu_count()
Parallel(n_jobs=num_cores)(delayed(crack)(oneLine) for oneLine in [line.rstrip('\n') for line in open('test.txt')])
