from django.urls import path

from bookapp.views import about, contact, home, books, send_json, contact

urlpatterns = [
    path('', home),
    path('books/', books),
    path('about/', about),
    path('send/', send_json),
    path('contact/', contact),

]
