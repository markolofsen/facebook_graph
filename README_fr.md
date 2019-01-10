<p align="center"><b>🛠️ Ce référentiel a été créé en utilisant le <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://gitupload.com"><img src="https://github.com/markolofsen/facebook_graph//blob/master/.banners/banner_fr.jpg?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/facebook_graph/blob/master/README_de.md">Deutsch</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README.md">English</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_es.md">Spanish</a> | <b>French</b> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_it.md">Italian</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_ru.md">Russian</a></p>

---

## Comment fonctionne le robot Facebook Graph?
Vous pouvez utiliser le débogueur de partage pour voir les informations utilisées lorsque le contenu de votre site Web est partagé sur Facebook, Messenger et d'autres endroits.


<a href="https://developers.facebook.com/tools/debug/accesstoken/">Accéder au jeton</a>


### Chaud à installer

```sh
pip3 install facebook_graph==0.0.1
```


### Comment utiliser

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
Nom de la bibliothèque = facebook_graph <br />
Titre = Facebook Graph crawler work <br />
Mots-clés = facebook,  graph,  api,  sharing,  share,  tool,  debug,  crawler <br />


---

<p align="center"><b>🛠️ Ce référentiel a été créé en utilisant le <a href="https://gitupload.com">GitUpload</a>.</b></p>