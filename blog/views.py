# coding:utf-8
from django.shortcuts import  render
from django.http import HttpResponse
from .models import Employee
# 引入我们创建的表单类
from .forms import AddForm
from django.template import RequestContext 
from django.views.decorators.csrf import requires_csrf_token

@requires_csrf_token
def index(request):
	user=Employee.objects.all()
	form = AddForm()
	if request.method == 'POST':
		form = AddForm(request.POST)
		if form.is_valid():
			name= form.cleaned_data['name']
			age= form.cleaned_data['age']
			gender= form.cleaned_data['gender']
			u=Employee(name=name,age=age,gender=gender)
			u.save()
           
	return render(request, 'index.html', {'form':form, 'user':user})
