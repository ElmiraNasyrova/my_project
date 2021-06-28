import argparse
import re
from collections import defaultdict
from subprocess import check_output


parser = argparse.ArgumentParser(description='Process access.log')
parser.add_argument('-f', dest='file', action='store', help='Path to logfile')
args = parser.parse_args()
filename = args.file


def wc(file_name):
    result = int(check_output(f'wc -l {file_name}', shell=True).split()[0])
    print('Всего выполнено запросоов:', result)


def grep(file_name, method):
    result = int(check_output(f'grep -i {method} {file_name} -c', shell=True))
    print(f'Выполнено {method}-запросов: {result}')


def search_top_ip(file_name):
    dict_ip = defaultdict(int)

    with open(file_name) as file:
        for line in file:
            ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
            if ip_match is not None:
                ip = ip_match.group()
                dict_ip[ip] += 1

    sorted_ip = sorted(dict_ip.items(), key=lambda x: x[1], reverse=True)

    for k in range(3):
        print(sorted_ip[k])


def search_most_long_request(file_name):
    max_time=0
    with open(file_name) as file:
        for line in file:
            time_match = re.search(r'.\d{1,9} \"-\"', line)
            if time_match is not None:
                time = int(time_match.group().replace(' "-"', ''))
                if time > max_time:
                    max_time = time

    print("Самый долгий запрос длится:", max_time)

# print_top_ip(filename)
# wc(filename)
# grep(filename, 'GET')
# search_most_long_request(filename)
