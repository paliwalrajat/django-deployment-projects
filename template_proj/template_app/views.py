from django.shortcuts import render

# Create your views here.
def index(request):
    my_dic = {'text':'my name is rajat paliwal','number':100}
    return render(request,'template_app/index.html',my_dic)

def other(request):
    return render(request,'template_app/other.html')

def relative(request):
    return render(request,'template_app/relative_url_temp.html')
