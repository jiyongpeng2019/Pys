# coding:utf-8


import threading


def add(a, b):
    print(a + b)


def moving(c):
    print("看电影 %s", c)


balance = 0


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
    if balance != 0:
        print(balance)


def run_thread(n):
    for j in range(10000):
        change_it(n)


if __name__ == "__main__":
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # if balance != 0:
    # print(balance)

    """
    t1 = threading.Thread(target=add, args=(1, 3))
    t2 = threading.Thread(target=moving, args="流")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    """
