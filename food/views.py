from django.shortcuts import render


def index(request):
    if request.method == 'GET':
        print("GET "*10)
        return render(request, 'food/index.html')
    elif request.method == 'POST':
        print(request.body)
