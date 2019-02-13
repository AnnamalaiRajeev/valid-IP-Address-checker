import sys
import re


def funct_parse(string_list):
    valid_ip_list = []
    for element in string_list:
        string_list_numbers = element.split(".")
        count = 0
        for number in string_list_numbers:
            number = int(number)
            if number in range(0, 256):
                count += 1
                if count == 4:
                    valid_ip_list.append(element)
    return valid_ip_list


with open("yo.txt") as fi:
    for line in fi:
        string_list = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
        valid_ip = funct_parse(string_list)
        print(valid_ip)

