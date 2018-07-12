import requests

def get_departures(src_url):
    resp = requests.get(src_url)

    if resp.status_code != 200:
        raise requests.ConnectionError('Received status {}'.format(resp.status_code))
        return None
    else:
       return resp
