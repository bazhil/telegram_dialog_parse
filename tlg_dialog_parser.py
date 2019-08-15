# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os

def tlg_parser(html):
    """
    Parse downloaded html-file with telegrsam chat
    :param html: html-file
    :return:
    """
    chat_text = ''

    with open(html, 'r', encoding='utf-8') as page:
        soup = BeautifulSoup(page.read(), 'html.parser')
        select = soup.find_all('div', {'class': 'text'})
        messages = [str(message.string) for message in select]
        for message in messages:
            chat_text += message

    with open('chat.txt', 'w', encoding='utf-8') as txt:
        print(chat_text, file=txt)

if __name__ == '__main__':
    work_dir = os.getcwd()
    for file in os.listdir(work_dir):
        if file.endswith('html'):
            tlg_parser(file)