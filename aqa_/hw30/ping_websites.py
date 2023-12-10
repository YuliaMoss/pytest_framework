""" 1 -

Створити метод який виводить в консоль пінг сайтів
Команда для Windows: ping -n 3 www.google.com
і для лінукс систем: ping -с 3 www.google.com
як параметри функція отримує список сайтів(пінг яких треба перевірити) та кількість запитів як у прикладі.
Метод універсальний відпрацьовує на будь якій ОС"""

import subprocess
import platform


def make_ping(websites_list):
    ping_results = []
    for website in websites_list:
        try:
            if platform.system().lower() == 'windows':
                ping_result = subprocess.run(['ping', '-n', '3', website], shell=True, capture_output=True, text=True)
            else:
                ping_result = subprocess.run(['ping', '-c', '3', website], shell=True, capture_output=True, text=True)
            ping_results.append(ping_result)
        except subprocess.CalledProcessError as e:
            print(f"Error pinging {website}: {e}")
    return ping_results


def print_ping_result(website, result):
    result_ping_dict = {website: result}
    return result_ping_dict


if __name__ == '__main__':
    websites_list_ping = ['www.google.com', 'www.youtube.com', 'www.datacamp.com']
    result_of_make_ping = make_ping(websites_list_ping)
    print(result_of_make_ping)
