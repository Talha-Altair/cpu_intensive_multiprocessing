import looper
from time import sleep

if __name__ == '__main__':

    print('-' * 20)
    print('Running load on CPU(s)')

    while True:

        print("sleeping for 100 seconds")

        sleep(15)

        print("running load on CPU(s)")

        looper.stress()

        print('-' * 20)