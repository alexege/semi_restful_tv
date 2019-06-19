from django.shortcuts import render, HttpResponse, redirect
from . import models

#Landing page - Render shows.html
#Localhost:8000
def index(request):
    pass
    context = {
        'all_shows' : models.Show.objects.all()
    }
    return render(request, "semi_restful_tv_app/shows.html", context)

#Return a template containing the form for adding a new show
#Localhost:8000/shows/new - GET
def new_shows(request):
    return render(request, "semi_restful_tv_app/new_show.html")

#Add a new show to the database, then redirect to /shows/<id>
#Localhost:8000/shows/create - POST
def shows_create(request):

    #Add a new item to the database
    models.Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])

    #Get id of last added Show
    id = models.Show.objects.last().id

    #Print newly added item properties to console
    print("Added a new item to the database, with the following properties:")
    print("title: " + request.POST['title'])
    print("network: " + request.POST['network'])
    print("release_date: " + request.POST['release_date'])
    print("description: " + request.POST['description'])

    return redirect('/shows/' + str(id))

#Return a tmeplate displaying the specific show's information
#Localhost:8000/shows - GET
def show_description(request, id):
    context = {
        'new_show' : models.Show.objects.get(id=id)
    }
    return render(request, "semi_restful_tv_app/show_details.html", context)

#Localhost:8000/shows/<id>/edit
def show_id_edit(request, id):
    context = {
        'show' : models.Show.objects.get(id=id)
    }
    #Add logic to update fields
    return render(request, 'semi_restful_tv_app/edit_show.html', context)

#Localhost:8000/shows/<id>/update
def show_id_update(request, id):
    show_to_update = models.Show.objects.get(id=id)
    print("show to update: " , show_to_update.title)
    show_to_update.title = request.POST['title']
    show_to_update.network = request.POST['network']
    show_to_update.release_date = request.POST['release_date']
    show_to_update.description = request.POST['description']
    show_to_update.save()
    return redirect('/shows/' + str(id))

#Localhost:8000/shows/<id>/delete
def show_id_delete(request, id):
    show_to_delete = models.Show.objects.get(id=id)
    show_to_delete.delete()
    return redirect('/')


#Destroy all items in the database
def delete_database(request):
    models.Show.objects.all().delete()
    return redirect('/')