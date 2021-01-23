from django.shortcuts import render
from django.http import HttpResponse
from . models import Student as st

# Create your views here.
def index(request):
    return HttpResponse('<h1>This is my index page</h1>')
def view(request):
    #return HttpResponse('<h2 text="red">This is my view page</h2>')
    return render(request,'view.html')

def edit(request):
    k=st.objects.all()
    if (k.count()==0):
        html = 'No such student'
    else:
        html='''
        <h2>LIST OF STUDENTS</h2><br><hr>
        <table border=2> <tr><th>Name</th><th>Place</th><th> Marks</th></tr>
        '''
        for i in k:
            html+='<tr><td>'
            html+=i.stname
            html+='</td><td>'
            html+=i.place
            html+='</td><td>'
            html+=str(i.mark)
            html+='</td></tr>'
        html+='</table>'



    return HttpResponse(html)
