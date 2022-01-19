import threading
from threading import Lock


# main function
def print_ln(lk, number, text):
    lk.acquire()
    print(f'{number}||{text}')
    lk.release()


def main():
    # Создаем блокиратор потока
    lk = Lock()
    # Создаем поток и передаем ему функцию для исполнения и аргументы
    # Обозначаем поток как демона
    # text = [input().split(" ")]
    text = "das asd fsd fzd".split(" ")
    for i in range(4):
        thr = threading.Thread(target=print_ln, args=(lk, i + 1, text[i]))
        # Запускаем выполнение потока
        thr.start()
        # Ждем завершения потока и не завершаем программу
        thr.join()


if __name__ == '__main__':
    main()
