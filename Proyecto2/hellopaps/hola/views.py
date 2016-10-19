from django.shortcuts import render, HttpResponse
from django.views.generic import View

class Hola(View):
	def get(self,request):
		return HttpResponse("Hasta que se puedo entrar tO.0")

# Create your views here.
