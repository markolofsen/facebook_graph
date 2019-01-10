<p align="center"><b>🛠️ Dieses Repository wurde mit <a href="https://gitupload.com">GitUpload</a> erstellt.</b></p>
<p align="center"><a href="https://gitupload.com"><img src="https://github.com/markolofsen/facebook_graph//blob/master/.banners/banner_de.jpg?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><b>Deutsch</b> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README.md">English</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_es.md">Spanish</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_fr.md">French</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_it.md">Italian</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_ru.md">Russian</a></p>

---

## Wie funktioniert der Facebook Graph-Crawler?
Mit dem Sharing Debugger können Sie die Informationen anzeigen, die verwendet werden, wenn Ihre Website-Inhalte auf Facebook, Messenger und anderen Orten geteilt werden.


<a href="https://developers.facebook.com/tools/debug/accesstoken/">Zugriffstoken erhalten</a>


### Heiß zu installieren

```sh
pip3 install facebook_graph==0.0.1
```


### Wie benutzt man

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
Bibliotheksname = facebook_graph <br />
Titel = Facebook Graph crawler work <br />
Schlüsselwörter = facebook,  graph,  api,  sharing,  share,  tool,  debug,  crawler <br />


---

<p align="center"><b>🛠️ Dieses Repository wurde mit <a href="https://gitupload.com">GitUpload</a> erstellt.</b></p>