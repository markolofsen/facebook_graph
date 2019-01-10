<p align="center"><b>🛠️ This repository was created using the <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://gitupload.com"><img src="https://github.com/markolofsen/facebook_graph//blob/master/.banners/banner_en.jpg?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/facebook_graph/blob/master/README_de.md">Deutsch</a> | <b>English</b> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_es.md">Spanish</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_fr.md">French</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_it.md">Italian</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_ru.md">Russian</a></p>

---

## How does the Facebook Graph crawler work?
You can use the Sharing Debugger to see the information that is used when your website content is shared on Facebook, Messenger and other places.


<a href="https://developers.facebook.com/tools/debug/accesstoken/">Get access token</a>


### Hot to install

```sh
pip3 install facebook_graph==0.0.1
```
                    

### How to use

```python
from facebook_graph import FBGRAPH

s = FBGRAPH().applyShare(
      token='****',
      link='https://gitupload.com',
      debug=False,
			wait=True,
    )

print(s)

#response
response = {
    "url": "https://gitupload.com/en",
    "type": "website",
    "title": "Best Git Marketing Tool",
    "image": [
        {
            "url": "https://gitupload.com/media/site_preview.jpg"
        }
    ],
    "updated_time": "2019-01-10T13:38:50+0000",
    "id": "2373231789364257"
}


```
                

<hr />


Version = 0.0.1 <br />
Library name = facebook_graph <br />
Title = Facebook Graph crawler work <br />
Keywords = facebook,  graph,  api,  sharing,  share,  tool,  debug,  crawler <br />

    

---

<p align="center"><b>🛠️ This repository was created using the <a href="https://gitupload.com">GitUpload</a>.</b></p>