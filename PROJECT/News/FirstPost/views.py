from django.shortcuts import render,redirect
from .models import NewsArticles
from .forms import NewsArticlesForm
def show(request):
    data = NewsArticles.objects.all()
    context = {
        'data' : data
    }
    return render(request, 'show.html', context)
def addarticle(request):
    form= NewsArticlesForm()
    if request.method == 'POST':
        form = NewsArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'addarticle.html', {'form': form})


def fulldetail(request, pk):
    data = NewsArticles.objects.get(id=pk)
    return render(request, 'fulldetail.html', {'data' : data})



def updatearticle(request, pk):
    data = NewsArticles.objects.get(id=pk)
    form = NewsArticlesForm(instance=data)
    if request.method == 'POST':
        form = NewsArticlesForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'updatearticle.html', {'form': form})


def deletearticle(request, pk):
    data = NewsArticles.objects.get(id=pk)
    data.delete()
    return redirect('home')
