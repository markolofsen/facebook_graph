<p align="center"><b>🛠️ Questo repository è stato creato usando <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://gitupload.com"><img src="https://github.com/markolofsen/facebook_graph//blob/master/.banners/banner_it.jpg?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/facebook_graph/blob/master/README_de.md">Deutsch</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README.md">English</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_es.md">Spanish</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_fr.md">French</a> | <b>Italian</b> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_ru.md">Russian</a></p>

---

## Come funziona il crawler di Facebook Graph?
Puoi utilizzare il Condivisore di condivisione per visualizzare le informazioni che vengono utilizzate quando il contenuto del tuo sito web è condiviso su Facebook, Messenger e altri luoghi.


<a href="https://developers.facebook.com/apps/">Ottieni client_id e client_secret</a> dalla tua app.


### Caldo da installare

```sh
pip3 install facebook_graph==0.0.3
```


### Come usare

```python
from facebook_graph import FBGRAPH

s = FBGRAPH(client_id='****', client_secret='****').applyShare(
        link='https://gitupload.com',
        debug=False,
        wait=True,
    )

print(s)

#response---------------->
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


Versione = 0.0.3 <br />
Nome libreria = facebook_graph <br />
Title = Facebook Graph crawler work <br />
Parole chiave = facebook,  graph,  api,  sharing,  share,  tool,  debug,  crawler <br />


---

<p align="center"><b>🛠️ Questo repository è stato creato usando <a href="https://gitupload.com">GitUpload</a>.</b></p>