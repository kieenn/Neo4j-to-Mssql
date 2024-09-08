from django.shortcuts import render
from neo4jtomssql.models import Menu
# Create your views here.
def index(request):

    menus = Menu.objects.all()

    context = {'menus': menus}
    return render(request, 'home/form.html', context)