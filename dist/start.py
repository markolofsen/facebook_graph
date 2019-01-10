import requests, threading, json

def jprint(arr):
    print(json.dumps(arr, indent=4, sort_keys=False))


class FBGRAPH():

    def applyShare(self, token, link, debug=False, wait=False):

        def get():
            url = 'https://graph.facebook.com/?scrape=true&access_token={access_token}&id={id}'.format(
                access_token=token,
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
    s = FBGRAPH().applyShare(
        token='****',
        link='https://gitupload.com',
        debug=True,
        wait=False,
    )
    print(s)
