from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
arr=['Java','Python',"CPP", 'C', 'DotNET',"SQL",'RDBMS','Django',"React","NOde","Javascript","PHP","Swift"]
globalcnt=dict()

def main(request):
    mydictionary={
        'arr':arr,
    }
    return render(request,"index.html",context=mydictionary)

def getquery(request):
  
    q=request.GET['languages']
    
    if q in globalcnt:
        globalcnt[q]+=1
    else:
        globalcnt[q]=1
        # error=False
    mydict={
        
        "arr":arr,
        "globalcnt":globalcnt,
    }
    return render(request,"index.html",context=mydict)