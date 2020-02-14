from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import MovieModel


class MovieView(ListView):
    model = MovieModel
    template_name = 'movie_list.html'
    paginate_by = 2


class MovieDetail(DetailView):
    model = MovieModel
    template_name = 'movie_list.html'


class MovieSearch(ListView):
    model = MovieModel
    template_name = 'movie_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        print(query)
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
            print(object_list)
        else:
            object_list = self.model.objects.none()
        return object_list
