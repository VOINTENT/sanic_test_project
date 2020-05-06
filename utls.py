from config import FILENAME
import json


def get_data():
    with open(FILENAME, 'r') as f:
        return json.load(f)


def read_urls(filename='urls.txt'):
    with open(filename, 'r') as f:
        urls = [row.strip() for row in f.readlines()]
        return urls
