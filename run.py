import json
import urllib.request

import settings
from line.line import APIClient


def get_gtrends() -> dict:
    """
    """
    res = {}
    try:
        url = 'https://gtrends-api-ss.herokuapp.com/'
        req = urllib.request.urlopen(url)
        res = json.loads(req.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('urllib.error: ', e)
    except json.JSONDecodeError as e:
        print('json.JSONDecodeError: ', e)

    return res

def run():
    """
    """
    line_bot_api = APIClient(settings.my_channel_access_token)
    data = get_gtrends()

    for k, v in data.items():
        line_bot_api.default_sender(v)


if __name__ == "__main__":
    run()
