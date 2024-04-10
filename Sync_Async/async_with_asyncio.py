# АСИНХРОННЫЙ КОД с использованием import asyncio  -->
# код быстрее выполняеться
import asyncio
import time


# -----   ПРИМЕР 1   -----------------------------------------------------------------------------------------------------
# ключевое слова async указывает, что функции асинхронные и их можна использовать
# коротины - ето название для асинхронныйх функций
async def print1():
    print(1)


async def print2():
    # asyncio.sleep остановка выполнение етой функции на 10 сек.
    # await ключевое слово для вызова асинхронных функций (коротинов)
    await asyncio.sleep(10)
    print(2)


async def print3():
    print(3)


async def main():
    # каждую асинхроную функцию нужно присоединять к задаче
    # создание tasks (тасков)
    # task1 = asyncio.create_task(print1())
    # task2 = asyncio.create_task(print2())
    # task3 = asyncio.create_task(print3())

    # создание tasks (тасов по другому)

    # Можно вызывать задачи (tasks) каждую отдельно
    # await task3
    # await task2
    # await task1

    # # вожно вызвать все задачи вместе
    # await asyncio.gather(tg)

    # создание tasks (тасков) + их выполнение
    async with asyncio.TaskGroup() as tg:
        tg.create_task(print1())
        tg.create_task(print2())
        tg.create_task(print3())


# запускаем событийныфй цикл , цикл к котором происходит перееключение и взаемодействие меожду функциями
# await не используется событийном цикле
asyncio.run(main())


# -----   ПРИМЕР 2   --------------------------------------------------------------------------------------------
# делаем вид что запрашиваем данные из сервера
async def get_data(url):
    print(f"Start...{url}")
    await asyncio.sleep(0.5)
    print(f"Done...{url}")
    return f"Data from {url}"


async def main():
    # используем генератор списков
    url = [f"www{i}" for i in range(5)]
    tasks = []
    for url in url:
        task = asyncio.create_task(get_data(url))
        tasks.append(task)
    for task in tasks:
        # await task возвращает return f"Data from {url}" из get_data
        await task


# start = time.time()
# asyncio.run(main())
# end = time.time()
# print(f"Time -> {end-start}")
