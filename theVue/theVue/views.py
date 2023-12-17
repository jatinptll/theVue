from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from service.models import Post_content

def home(request):
    pass_data={}
    try:
        if request.method=="POST":
            data=request.POST.get("content")
            print(data)
            if data!="":
                content=Post_content(content=data)
                content.save()

                get_data=Post_content.objects.all()

                pass_data={
                    "back_data":get_data
                }   

    except:
        pass


    return render(request, 'index.html',pass_data) 

def trending(request):

    return render(request, 'trending.html') 

def aboutus(request):

    return render(request, 'aboutus.html') 



    