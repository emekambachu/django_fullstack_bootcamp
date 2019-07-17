from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# import view and Template view for class based views
from django.views.generic import View, TemplateView

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