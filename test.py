from multiprocessing import Process
import time

def print_hello(name):
    time.sleep(3)
    print('hello ' + name)

def main():
    process = Process(target=print_hello, args=('001',))
    process.start()
    # process.join()
    # process.terminate()

if __name__ == '__main__':
    main()

