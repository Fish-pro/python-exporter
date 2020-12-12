import threading

import requests


def worker():
    res = requests.get("http://127.0.0.1:5000").text
    print(res)


def run():
    for i in range(100000):
        threading.Thread(target=worker())


if __name__=="__main__":
    run()