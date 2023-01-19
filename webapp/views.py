from django.shortcuts import render, redirect
from .solver import solve
from django.http import HttpResponse
from django.template import loader
from .classes_OOP import Game
from .classes_OOP import Ball

tubes_collection = []
tube = []
tube_size_user = 0 # The tube_size value defined by users
solution_index = 0
solution = []

# Create your views here.
def index(request):
    global tube_size_user, tubes_collection, tube, solution

    if(request.method == "POST"):
        list_of_tubes = []

        # if Save Tubesize button is clicked
        if "save-tubesize" in request.POST:
            tube_size_user = int(request.POST.get("tube_size"))


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

def display_game(game):
    '''
    Convert a game's tubes_lst to to list of Ball objects for display
    '''
    counter = 100 * tube_size_user
    game_balls_display = []
    tube = []

    for i in game.tubes_lst:
        for j in range(len(i)-1, -1, -1):
            temp_ball = Ball(i[j], counter - 50)
            counter -= 100
            tube.append(temp_ball)

        game_balls_display.append(tube)
        counter = 100*tube_size_user
        tube = []

    return game_balls_display

# print(display_game(Game(2, [['blue', 'red'], ['blue', 'red'], []])))

def solution(request):
    global solution, solution_index
    '''
    Display the solution output
    '''
    
    # If a solution exists
    if(type(solution) == list):

        # Detect button clicks for next steps/ previous steps
        if(request.method == "POST"):
            # Change index value to iterate through solution
            if "next" in request.POST:
                solution_index += 1 
            
            else:
                solution_index -= 1

        # Avoid index out of range due to spamming the buttons
        if (solution_index < 0):
            solution_index = 0

        elif (solution_index >= len(solution)):
            solution_index = len(solution)-1

        output_display_game = display_game(solution[solution_index])

    # If a solution does not exist
    else:
        output_display_game = solution

    return render(request, 'solution.html', {'output': output_display_game, 'tube_size': tube_size_user})

def navbar_render(request):
    navbar = loader.get_template('navbar.html')
    return HttpResponse(navbar.render())

def add_tubes(request):
    '''
    Render the add_tubes page
    '''

    global tubes_collection, tube, counter, tube_size_user

    if (request.method == "POST"):
        counter = 100 * tube_size_user

        for i in range (int(request.POST.get("ball-num", None)),0,-1):
            # Generate Ball objects for HTML canvas drawing
            temp = Ball(request.POST.get("ball-"+str(i), None), counter-50)
            # Adjust positions
            counter -= 100
            # Add the ball to the tube
            tube.append(temp)

        # Add tube to tubes_collection
        tubes_collection.append(tube)
        tube = []
        return redirect('../')

    return render(request, 'add-tubes.html')