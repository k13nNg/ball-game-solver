
from django.shortcuts import render, redirect
tubes_collection = []
tube = []
counter = 500

class Ball:
    color = ""
    y_pos = 0

    def __init__(self, c, yp):
        self.color=c
        self.y_pos=yp

    def get_color(self):
        return self.color

    def get_y_pos(self):
        return self.y_pos

# Create your views here.
def index(request):
    if(request.method == "POST"):
        list_of_tubes = []
        for i in tubes_collection:
            list_of_balls = []

            for j in i:
                # the ball at the top of the tube is the ball at the beginning of the list 
                # --> better to access arr[0] than arr[len(arr)-1]
                list_of_balls.insert(0, j.color)
                
            list_of_tubes.append(list_of_balls)

        print(list_of_tubes)


    return render(request, 'index.html', {'tubes_collection': tubes_collection})

def add_tubes(request):
    global tubes_collection, tube, counter

    if (request.method == "POST"):
        counter = 500
        for i in range (int(request.POST.get("ball-num", None)),0,-1):
            # temp = Ball.objects.create(y_pos= counter-50, color=request.POST.get("ball-"+str(i), None))
            temp = Ball(request.POST.get("ball-"+str(i), None), counter-50)
            counter -= 100
            tube.append(temp)

        
        tubes_collection.append(tube)
        tube = []
        return redirect('../index')

    return render(request, 'add-tubes.html')