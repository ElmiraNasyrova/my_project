import json
import datetime

from collections import defaultdict
from subprocess import run, check_output


def ps_result():
    result = 0
    try:
        result = check_output(f'ps aux', shell=True).decode()
    except:
        pass
    return result


def get_data(input_data):
    dict_users_process = defaultdict(int)
    users_list = list()
    cpu = 0
    max_cpu = 0.
    mem = 0
    max_mem = 0.
    cpu_process = None
    mem_process = None

    for line in input_data:
        split_line = line.split()

        user_cpu = float(split_line[2])
        cpu += user_cpu

        if user_cpu > max_cpu:
            max_cpu = user_cpu
            cpu_process = split_line[len(split_line)-1]

        user_mem = float(split_line[3])
        mem += user_mem

        if user_mem > max_mem:
            max_mem = user_mem
            mem_process = split_line[len(split_line)-1]

        user = split_line[0]
        if user not in users_list:
            users_list.append(user)

        dict_users_process[user] += 1

    return dict_users_process, users_list, cpu, cpu_process, mem, mem_process


if __name__ == "__main__":
    res = ps_result().split('\n')
    data = res[1: len(res)-1]

    user_data, user_list, cpu_sum, cpu_proc, mem_sum, mem_proc = get_data(data)

    statistic_data = \
        f'"Пользователи системы:":{user_list}\n' \
        f'"Процессов запущено:": {len(data)}\n' \
        f'"Пользовательских процессов: ": {user_data}\n' \
        f'"Всего памяти используется, mb:": {round(mem_sum, 2)}\n' \
        f'"Всего CPU используется, %:": {round(cpu_sum, 2)}\n' \
        f'"Больше всего памяти использует:": {mem_proc[:20]}\n' \
        f'"Больше всего CPU использует:": {cpu_proc[:20]}'

    print(statistic_data)

    today = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")
    with open(f'{today}-scan.txt', 'w') as f:
        f.write(statistic_data)
