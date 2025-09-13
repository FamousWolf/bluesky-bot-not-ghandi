from atproto import Client
import random
import configparser

def random_line(file):
    return random.choice(list(open(file))).rstrip()

config = configparser.ConfigParser()
config.read('config.ini')

message = random_line('quotes.txt')

client = Client()
client.login(config['login']['Username'], config['login']['Password'])
post = client.send_post(message, langs=[config['language']['Language']])
