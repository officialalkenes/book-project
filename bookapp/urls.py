from django.urls import path

from bookapp.views import about, home, books

urlpatterns = [
    path('', home),
    path('books/', books),
    path('about/', about),

]
