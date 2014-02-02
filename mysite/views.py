from django.shortcuts import render
from django import template
from django.views.decorators.csrf import csrf_exempt
from paint.models import Paint


def welcome(request):
	return render(request, 'welcome.html')
	
def home(request):
	return render(request, 'home.html')
@csrf_exempt
def save(request):
	iname=request.POST.get('name')
	idata=request.POST.get('data')
	p=Paint(filename=iname,imagedata=idata)
	p.save()
	return render(request,'home.html')
def gallery(request):
	images=[dict(id=i.id,filename=i.filename) for i in Paint.objects.order_by('id')] 
	return render(request,'post.html',{'images':images})
def load(request,filen):
	data=Paint.objects.filter(filename=filen)	
	images=[dict(id=i.id,filename=i.filename,imagedata=i.imagedata) for i in Paint.objects.filter(filename=filen)]
	return render(request,'load.html',{'images':images})

		
