#!/usr/bin/env on-python3
# -*- coding: utf-8 -*-

import time, threading

# 线程执行的代码:
def loop():
    print('thread is starting')
    n = 0
    while n < 5:
        n = n + 1
        print('thread is running >>> %s' % (n))
        time.sleep(1)
    print('thread  ended.')

if __name__ == "__main__":
    print('main is starting...')
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('main is ended')
