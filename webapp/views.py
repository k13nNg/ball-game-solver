from django.shortcuts import render, redirect
from .solver import solve
from .classes_OOP import Game
from .classes_OOP import Ball

tubes_collection = []
tube = []
tube_size_user = 0 # The tube_size value defined by users
solution = []

# Create your views here.
def index(request):
    global tube_size_user, tubes_collection, tube, solution

    if(request.method == "POST"):
        list_of_tubes = []

        # if Save Tubesize button is clicked
        if "save-tubesize" in request.POST:
            tube_size_user = int(request.POST.get("tube_size"))
            print(tube_size_user)

        # if Reset button is clicked
        elif "reset" in request.POST:
            tubes_collection = []
            tube = []
            tube_size_user = 0
        
        # when Solve button is clicked
        elif "solve" in request.POST:
            for i in tubes_collection:
                list_of_balls = []

                for j in i:
                    # the ball at the top of the tube is the ball at the beginning of the list 
                    # --> better to access arr[0] than arr[len(arr)-1]
                    list_of_balls.insert(0, j.color)

                list_of_tubes.append(list_of_balls)

            input_game = Game(tube_size_user, list_of_tubes, 0)

            # The solution to the configure (if exists)
            solution = solve(input_game)

            # Redirect you to the solution display page
            return redirect('../solution')

    return render(request, 'index.html', {'tubes_collection': tubes_collection, 'tube_size': tube_size_user})

def solution(request):

    return render(request, 'solution.html', {'output': output_solution})

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