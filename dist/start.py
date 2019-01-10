import requests, threading, json

def jprint(arr):
    print(json.dumps(arr, indent=4, sort_keys=False))


class FBGRAPH(object):

    client_id, client_secret = '', ''

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def getToken(self):

        url = 'https://graph.facebook.com/oauth/access_token?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials'.format(
            client_id = self.client_id,
            client_secret = self.client_secret,
        )
        req = requests.post(url, data={}, headers={}, stream=True, verify=False)
        content = req.content.decode('utf-8')
        data = json.loads(content)

        return data['access_token']

    def applyShare(self, link, debug=False, wait=False):

        def get():
            url = 'https://graph.facebook.com/?scrape=true&access_token={access_token}&id={id}'.format(
                access_token=self.getToken(),
                id=link,
            )
            try:
                req = requests.post(url, data={}, headers={}, stream=True, verify=False)
                content = req.content.decode('utf-8')
                data = json.loads(content)
                if debug:
                    jprint(data)
                return data
            except Exception as e:
                return {
                    'error': True,
                    'message': e,
                }


        if wait:
            return get()
        else:
            threading.Thread(target=get, args=()).start()
            return {
                'error': False,
                'message': 'Success',
            }


if __name__ == "__main__":

    s = FBGRAPH(client_id='****', client_secret='****').applyShare(
        link='https://gitupload.com',
        debug=False,
        wait=True,
    )
    print(s)
    