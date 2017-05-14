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
    if request.method == 'POST':# 当提交表单时
    
        form = AddForm(request.POST) # form 包含提交的数据
        
        if form.is_valid():# 如果提交的数据合法
            name= form.cleaned_data['name']
            age= form.cleaned_data['age']
            gender= form.cleaned_data['gender']
            u=Employee(name=name,age=age,gender=gender)
            u.save()
            print "OK"
            user=Employee.objects.all()
            return render(request, 'index.html', {'form':form, 'user':user})

    else:

        form = AddForm()
    return render(request, 'index.html', {'form':form, 'user':user})