from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# import view and Template view for class based views
from django.views.generic import View, TemplateView, ListView, DetailView

from . import models

# Function based view
# def index(request):
#     return render(request, 'cbvapp/index.html')

class CBView(View):
    def get(self, request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL")

class IndexView(TemplateView):
    template_name = 'cbvapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['insert'] = 'BASIC INJECTION'
        return context

class SchoolListView(ListView):
    # (automatically returns school_list to view, if context_object_name is not there)

    # change school_list to schools
    context_object_name = 'schools'

    # import school model
    model = models.School

class SchoolDetailView(DetailView):
    # (automatically returns only school to view, if context_object_name is not there)
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'cbvapp/school_detail.html'