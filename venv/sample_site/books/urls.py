from django.conf.urls import url
from django.urls import path
from .views import index , genre, get_book, by_id, get_params, get_book_by_id, create_book, submit, get_author_by_id

app_name = "books"

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^genre', genre, name="genre"),
    path('get_book/<int:index>', get_book),
    url(r'^by_id/(?P<index>[1-70]+)$', by_id),
    url(r'^params/', get_params),
    path('get_book_by_id/<int:id>', get_book_by_id),
    # new !!!
    url(r'^create/', create_book, name="create"),
    # url(r'^submit$', submit, name="submit"),
    path('get_author_by_id/<int:id>', get_author_by_id, name="get_author"),
]