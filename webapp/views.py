
from django.shortcuts import render, redirect
tubes_collection = []
tube = []
tube_size_user = 0 # The tube_size value defined by users


class Game:
    tube_size = 0
    max_colors = 0
    tubes_lst = []

    def __init__(self, tube_size, lst_of_tubes):
        self.tubes_lst = lst_of_tubes
        self.max_colors = len(lst_of_tubes)
        self.tube_size = tube_size


class Ball:
    color = ""
    y_pos = 0

    def __init__(self, c, yp):
        self.color=c
        self.y_pos=yp

# Create your views here.
def index(request):
    global tube_size_user, tubes_collection, tube

    if(request.method == "POST"):
        list_of_tubes = []

        if "save-tubesize" in request.POST:
            tube_size_user = int(request.POST.get("tube_size"))
            print(tube_size_user)

        if "reset" in request.POST:
            tubes_collection = []
            tube = []
            tube_size_user = 0
        
        else:
            for i in tubes_collection:
                list_of_balls = []

                for j in i:
                    # the ball at the top of the tube is the ball at the beginning of the list 
                    # --> better to access arr[0] than arr[len(arr)-1]
                    list_of_balls.insert(0, j.color)

                    
                    
                list_of_tubes.append(list_of_balls)


    return render(request, 'index.html', {'tubes_collection': tubes_collection, 'tube_size': tube_size_user})

def add_tubes(request):
    global tubes_collection, tube, counter, tube_size_user

    if (request.method == "POST"):
        counter = 100 * tube_size_user

        for i in range (int(request.POST.get("ball-num", None)),0,-1):
            temp = Ball(request.POST.get("ball-"+str(i), None), counter-50)
            counter -= 100
            tube.append(temp)

        
        tubes_collection.append(tube)
        tube = []
        return redirect('../index')

    return render(request, 'add-tubes.html')