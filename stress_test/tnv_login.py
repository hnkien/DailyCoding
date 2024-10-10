
# Stress test TN
import requests
import random
import string
import logging
import threading
from time import sleep

url = "https://api-v5.trangnguyen.edu.vn/v5/users/loginV0"

def login_Student(account):
    try:
        account_name, account_password = account.split(",")
    except ValueError:
        account_name = None
        account_password = None

    if account_name and account_password:
        data = {
            "username": account_name,
            "password": account_password
        }

        # print(data)

        response = requests.post(url, json=data)
        # print("Status Code", response.status_code)
        if response.status_code == 200:
            print(f"OK : {account_name}")
            # print(f"OK : {account_name} - {response.json()}")
        else:
            print(f"Fail: {response.json()}")
            # pass


def run_single(file_account):
    data = file_account.read()
    data_list = data.split("\n")
    while True:
        # print(random.choice(data_list))
        login_Student(random.choice(data_list))
        sleep(0.01)


def run_thread(nThread, file_account):
    threads = list()
    for index in range(nThread):
        # logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=run_single, args=(file_account,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        # logging.info("Main    : before joining thread %d.", index)
        thread.join()
        # logging.info("Main    : thread %d done", index)


if __name__ == '__main__':
    with open("account_TN.txt", 'r') as file_account:
        # run_single(file_account)
        run_thread(200, file_account)



