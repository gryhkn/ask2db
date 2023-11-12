## Database'e Sor

Bu küçük uygulama Langchain ve OpenAI kullanarak PostgreSQL database'inden SQL sorgusu yazmadan
bilgi çekmeyi sağlıyor. Bunun için yerelde veya uzakta çalışan bir db'ye ve requirements.txt'deki kütüphanelere ihtiyacınız var. 

<hr>

### Kurulum

```
1) git clone https://github.com/gryhkn/ask2db.git
2) cd ask2db
3) python -m venv venv (bu son venv yerine istediğiniz virtual env. ismi yazın)
4) pip3 install -r requirements.txt (pip3 çalışmazsa pip yazın)
```

Yukarıdaki adımları sorunsuz yaptıysanız, şimdi de ``` .copy env ```dosyasını ```.env``` olarak değiştirip kendi OpenAI API keyinizi girin.

Ve son olarak aşağıdaki komutu yazın.
```
5) python main.py
```

<hr>

<br>
Ekran görüntüsü

![ss](https://github.com/gryhkn/ask2db/blob/master/img.png)

<br>

#### Kaynak

https://python.langchain.com/docs/use_cases/qa_structured/sql