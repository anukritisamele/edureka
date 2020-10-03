from django.http import HttpResponse
from django.shortcuts import render
#from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required
def home(request):
    return render(request, 'home.html', {'title':'django'})

'''def loggedin(request):#que = "select  products.product_name,patch_orgs_info.product_id,patch_orgs_info.patch_login from" \
  return render(request,'base.html',extra_context)

@login_required'''
def profile(request):
    return HttpResponse("profile page")

def expression(request):
    a = int(request.GET['text1'])
    b = int(request.GET['text2'])
    c = a+2*a*b
    return render(request,'output.html', {'result':c})

# def login(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['id']
#         password = request.POST['pass']
#         return render(request,'login.html')


def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def news(request):
    return render(request, 'news.html')