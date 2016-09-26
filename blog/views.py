from django.shortcuts import render_to_response
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import Employee

# Create your views here.
class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex= sex

    def say(self):
        return  "I'm " + self.name 

def index(req):
    user = {'name':'tom','age':23,'sex':'male'}
    book_list = ['python','java','php','web']
    uu = Person('tttom',233,'male')
    emps = Employee.objects.all()
    t = loader.get_template("index.html")
    c = Context({'title':'my page','book_list':book_list,'user':user,'emps':emps})

    

    return HttpResponse(t.render(c))

