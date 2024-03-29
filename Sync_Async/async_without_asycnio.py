# АСИНХРОННЫЙ КОД без import asyncio  -->
# функиции clock и query работают паралельно
# правило, чтоб у функций не было функционала,который заблокируем поток выполнения ( например input() )
import time
import os


def clock():
    time0 = round(time.time())
    while True:
        if round(time.time() - time0) % 5 == 0:
            yield "5 sec"
        else:
            yield 0


def query():
    # вывод все файл в указаном томе
    for i in os.walk("D:\\"):
        yield i[0]


def main():
    data = query()
    alarm = clock()
    while True:
        d = next(data)
        a = next(alarm)
        print(d)
        if a:
            print(a)
        time.sleep(1)


main()
