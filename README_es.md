<p align="center"><b>🛠️ Este repositorio fue creado usando el <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://gitupload.com"><img src="https://github.com/markolofsen/facebook_graph//blob/master/.banners/banner_es.jpg?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/facebook_graph/blob/master/README_de.md">Deutsch</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README.md">English</a> | <b>Spanish</b> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_fr.md">French</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_it.md">Italian</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_ru.md">Russian</a></p>

---

## ¿Cómo funciona el rastreador de gráficos de Facebook?
Puede usar el Depurador de uso compartido para ver la información que se usa cuando el contenido de su sitio web se comparte en Facebook, Messenger y otros lugares.


<a href="https://developers.facebook.com/tools/debug/accesstoken/">Obtener token de acceso</a>


### Caliente para instalar

```sh
pip3 install facebook_graph==0.0.2
```


### Cómo utilizar

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


Versión = 0.0.2 <br />
Nombre de la biblioteca = facebook_graph <br />
Título = Facebook Graph crawler work <br />
Palabras clave = facebook,  graph,  api,  sharing,  share,  tool,  debug,  crawler <br />


---

<p align="center"><b>🛠️ Este repositorio fue creado usando el <a href="https://gitupload.com">GitUpload</a>.</b></p>