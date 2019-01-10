<p align="center"><b>🛠️ Этот репозиторий был создан с использованием <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://gitupload.com"><img src="https://github.com/markolofsen/facebook_graph//blob/master/.banners/banner_ru.jpg?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/facebook_graph/blob/master/README_de.md">Deutsch</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README.md">English</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_es.md">Spanish</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_fr.md">French</a> | <a href="https://github.com/markolofsen/facebook_graph/blob/master/README_it.md">Italian</a> | <b>Russian</b></p>

---

## Как работает сканер графа Facebook?
Вы можете использовать Отладчик общего доступа, чтобы увидеть информацию, которая используется, когда контент вашего сайта публикуется в Facebook, Messenger и других местах.


<a href="https://developers.facebook.com/apps/">Получите client_id & client_secret</a> из вашего приложения.


### Горячая установка

```sh
pip3 install facebook_graph==0.0.3
```


### Как пользоваться

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


Версия = 0.0.3 <br />
Название библиотеки = facebook_graph <br />
Название = Facebook Graph crawler work <br />
Ключевые слова = facebook,  graph,  api,  sharing,  share,  tool,  debug,  crawler <br />


---

<p align="center"><b>🛠️ Этот репозиторий был создан с использованием <a href="https://gitupload.com">GitUpload</a>.</b></p>