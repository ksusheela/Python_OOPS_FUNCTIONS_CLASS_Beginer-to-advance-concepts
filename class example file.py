from time import sleep
from threading import *


class hello(Thread):
    def run(self):
        for i in range(10):
            print('hello')
            sleep(1)


class hi(Thread):
    def run(self):
        for i in range(10):
            print('hi')
            sleep(1)


t1 = hello()  # t1 is the object of hello method
t2 = hi()  # t2 is the objec of hi method

t1.start()
sleep(0.2)
t2.start()