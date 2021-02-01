import configparser


conf = configparser.ConfigParser()
conf.read('settings.ini')

my_channel_access_token = conf['line']['my_channel_access_token']
my_channel_secret = conf['line']['my_channel_secret']
