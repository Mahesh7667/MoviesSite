from django.urls import path
from .views import MovieView,MovieDetail ,MovieSearch

urlpatterns = [
    path('', MovieView.as_view(), name ='movie_list' ),
    path('search/' , MovieSearch.as_view() , name = "movie_search"),
]
