from django.http import JsonResponse, HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.serializers import Serializer
from .models import *
from .serializers import *
from .forms import *

class CreateProtein(mixins.CreateModelMixin, generics.GenericAPIView):
    protein_query = Protein.objects.all()
    serializer_class = ProteinSerializer
    form_class = ProteinForm

    def post(self,request, *args, **kwargs):
        return self.create(request, * args, **kwargs)

class protein_details(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Protein.objects.all()
    serializer_class = ProteinSerializer
    form_class = ProteinForm

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, * args, **kwargs)
