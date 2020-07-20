## Django URL Shortener
實作簡易的Django縮短網址服務.
於Heroku 架設 RestFul 縮短網址 API 服務.

**使用框架:**

 - Django
 - Django Rest Framework
 - Ajax

**Demo:** [https://james-shorturl.herokuapp.com/](https://james-shorturl.herokuapp.com/)

**API:**
URL: `https://url-shortener-drf.herokuapp.com/api/shorten-url/`
Method: `POST`
Body:

```json callback
{
"url": "https://www.google.com/"
}
```

**運行作法:**

 - 複製該專案
 - 切換路徑 `cd <project-folder>` 和運行 `pip install requirements.txt` 
 - 運行 `python manage.py makemigrations`和`python manage.py migrate` Migrate Model到資料庫
 - 測試發布: 運行`python manage.py runserver` 
