
from django.shortcuts import render, redirect

# temp_arr = []
tubes_collection = []
tube = []


# Create your views here.
def index(request):
    return render(request, 'index.html', {'tubes_collection': tubes_collection})

def add_tubes(request):
    global tubes_collection, tube

    if (request.method == "POST"):
        for i in range (1, int(request.POST.get("ball-num", None))+1):
            # print(request.POST.get("ball-"+str(i), None))
            tube.append(request.POST.get("ball-"+str(i), None))
        
        tubes_collection.append(tube)
        tube = []

        return redirect('../index')

    return render(request, 'add-tubes.html')