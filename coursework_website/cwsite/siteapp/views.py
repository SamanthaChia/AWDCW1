from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def index(request):
    proteins = Protein.objects.all()
    domains = Domain.objects.all()
    return render(request, 'siteapp/index.html', {'proteins':proteins})
