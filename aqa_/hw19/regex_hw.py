import re

my_string = ("Place of delivery of goods or place of performance of work or provision of services: 82172, Ukraine, "
             "Lviv Region, Stebnyk, str. Doroshenko, 1 Deadline for delivery of goods, performance of works or "
             "provision of services: 31.12.2023")

if __name__ == '__main__':
    data = {
        'country': re.search(r', ([A-Za-z]+), +', my_string).group(1),
        'region': re.search(r'[A-Z][a-z]{3} [A-Z][a-z]{5}', my_string).group(),
        'city': re.search(r'([A-Za-z]+),\s([a-z]+\.)', my_string).group(1),
        'postal': re.search(r'\d{5}', my_string).group(),
        'address': re.search(r'[a-z]{3}. [A-Z]+[a-z]{9}, [0-9]', my_string).group(),
        'deadline': re.search(r'\d{2}.\d{2}.\d{4}', my_string).group(),
    }
    print(data)
