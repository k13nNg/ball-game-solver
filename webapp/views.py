
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_tubes(request):
    if (request.method == "POST"):
        print()
        return redirect('../index')

    return render(request, 'add-tubes.html')