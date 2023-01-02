
from django.shortcuts import render, redirect
from webapp.models import Ball
# temp_arr = []
tubes_collection = []
tube = []
counter = 500



# Create your views here.
def index(request):
    return render(request, 'index.html', {'tubes_collection': tubes_collection})

def add_tubes(request):
    global tubes_collection, tube, counter

    if (request.method == "POST"):
        counter = 500
        for i in range (1, int(request.POST.get("ball-num", None))+1):
            temp = Ball.objects.create(y_pos= counter-50, color=request.POST.get("ball-"+str(i), None))
            counter -= 100
            print(type(temp.y_pos))
            tube.append(temp)
            print("y_pos: ", temp.y_pos)
        
        tubes_collection.append(tube)
        tube = []
        return redirect('../index')

    return render(request, 'add-tubes.html')