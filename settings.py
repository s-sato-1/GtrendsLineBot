import os
import configparser

is_release = True
if is_release:
    my_channel_access_token = os.environ.get("my_channel_access_token")
    my_channel_secret = os.environ.get("my_channel_secret")
else:
    conf = configparser.ConfigParser()
    conf.read('settings.ini')
    my_channel_access_token = conf['line']['my_channel_access_token']
    my_channel_secret = conf['line']['my_channel_secret']
