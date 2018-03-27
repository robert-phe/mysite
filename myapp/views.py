from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Test, Page


class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'test_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Test.objects.filter(page__test__isnull=False).distinct()



class DetailView(generic.DetailView):
    model = Test
    template_name = 'myapp/detail.html'

    # def get_queryset(self):
    #     """
    #     Excludes any questions that aren't published yet.
    #     """
    #     return Question.objects.filter(pub_date__lte=timezone.now())


    # def index(request):
    #     return HttpResponse("Hello, world")