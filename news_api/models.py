from django.db import models

# Create your models here.
"""

    "source": {
        "id": null,
        "name": "Gizmodo.com"
    },
    "author": "Andrew Liszewski",
    "title": "You Can Finally Buy Apple's Magic Keyboard with Touch ID Without Buying an iMac",
    "description": "Apple finally brought Touch ID to its desktop computers earlier this year with an upgraded version of its wireless Magic Keyboard featuring an added fingerprint sensor. To date, it’s been exclusively available with Apple’s new M1-powered iMac, but it now fina…",
    "url": "https://gizmodo.com/you-can-finally-buy-apples-magic-keyboard-with-touch-id-1847412879",
    "urlToImage": "https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/88ebfb3d69db4eb2742ccacb6266421c.jpg",
    "publishedAt": "2021-08-03T13:30:00Z",
    "content": "Apple finally brought Touch ID to its desktop computers earlier this year with an upgraded version of its wireless Magic Keyboard featuring an added fingerprint sensor. To date, its been exclusively … [+1608 chars]"
"""


class News(models.Model):
    author = models.CharField(max_length=100)
    title = models.TextField()
    description = models.TextField()
    url = models.CharField(max_length=500)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def get_information(self):
        return f"{self.title} written by: {self.author}"
