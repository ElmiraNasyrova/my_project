import argparse
import re
import os
import json

from collections import defaultdict
from subprocess import check_output

parser = argparse.ArgumentParser(description='Process access.log')
parser.add_argument('-p', dest='path', action='store', help='Path to logfile')
args = parser.parse_args()


def find_files(file_name):
    files_array = []

    for root, dirs, files in os.walk(file_name):
        for file in files:
            if file.endswith(".log"):
                log_file_path = os.path.join(root, file)
                files_array.append(log_file_path)

    return files_array


def grep(file_name, method="'[^ ]'"):
    result = 0
    try:
        result = int(check_output(f'grep {method} -c {file_name}', shell=True))
        if method == "'[^ ]'":
            method = 'всего '
        print(f'Выполнено {method}запросов: {result}')
    except:
        pass

    return result


def search_top_ip(file_name):
    top = 3
    dict_ip = defaultdict(int)

    with open(file_name) as file:
        for line in file:
            ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
            if ip_match is not None:
                ip = ip_match.group()
                dict_ip[ip] += 1

    sorted_ip = sorted(dict_ip.items(), key=lambda x: x[1], reverse=True)

    if len(sorted_ip) < top:
        top = len(sorted_ip)

    print("Самые частые запросы от:")
    for i in range(top): print(sorted_ip[i])

    return sorted_ip[0:top]


def search_most_long_request(file_name):
    time_array = []
    top = 3

    with open(file_name) as f:
        for line in f:
            line_split = line.split()
            time = line_split[len(line_split) - 1]
            time_array.append((int(time), line))

    sorted_time = sorted(time_array, key=lambda x: x[0], reverse=True)

    if len(sorted_time) < top:
        top = len(sorted_time)

    print("Самые долгие запросы:")
    for i in range(top): print(sorted_time[i])

    return sorted_time[0:top]


def get_data(file_for_get_data):
    requests_quantity = grep(file_for_get_data)
    get = grep(file_for_get_data, 'GET ')
    post = grep(file_for_get_data, 'POST ')
    put = grep(file_for_get_data, 'PUT ')
    delete = grep(file_for_get_data, 'DELETE ')
    head = grep(file_for_get_data, 'HEAD ')
    top_three_ip = search_top_ip(file_for_get_data)
    top_three_long_req = search_most_long_request(file_for_get_data)

    statistic_data = dict(
        requests_quantity=requests_quantity,
        GET=get,
        POST=post,
        PUT=put,
        DELETE=delete,
        HEAD=head,
        top_three_ip=top_three_ip,
        top_three_long_requests=top_three_long_req
    )
    file_name = os.path.basename(file_for_get_data).replace('.log', '')
    with open(f'statistic_data_{file_name}.json', 'w') as f:
        s = json.dumps(statistic_data, indent=4)
        f.write(s)


if __name__ == "__main__":
    if '.log' not in args.path:
        log_files = find_files(args.path)
        for file in log_files:
            print("Статистика по файлу: ", file)
            get_data(file)
    else:
        get_data(args.path)
