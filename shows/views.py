from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from .models import Shows

def index(request):
    return redirect('/shows')

def shows(request):
    allshows = Shows.objects.all()
    context={
    'shows': allshows,
    }
    return render(request, 'shows.html', context)
    

def new(request):
    if request.method == 'GET':
        return render(request, 'new_show.html')
    
    if request.method == 'POST':
        # print(request.POST)
        errors = Shows.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/shows/new")
        else:
            Shows.objects.create(title=request.POST['title'], release_date=request.POST['release_date'], network=request.POST['network'], description=request.POST['description'])
            messages.success(request, "Ha sido creado con exito")
            return redirect("/")
    

def edit(request, id):

    context = {
        'show' : Shows.objects.get(id=id)
    }
    if request.method == 'GET':
        return render(request, 'edit_shows.html', context)
    
    if request.method == 'POST':
        print(request.POST)
        errors = Shows.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/shows/{id}/edit")
        else:
            show = Shows.objects.get(id=id)
            show.title=request.POST['title']
            show.network=request.POST['network']
            show.description=request.POST['description']
            show.release_date=request.POST['release_date']
            show.save()
            return redirect(f"/shows/{id}")

def show(request, id):
    show2show= Shows.objects.get(id=int(id))
    print(show2show)
    context = {
        'shows' : show2show,
    }
    return render(request, 'tv_shows_dos.html', context)
    

def delete(request, id):
    context = {
        'show' : Shows.objects.get(id=id)
    }
    Shows.objects.get(id=id).delete()
    return redirect("/") 