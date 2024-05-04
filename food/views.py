import json

from django.http import JsonResponse
from django.shortcuts import render

from food.forms import PromoDayForm


def index(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print('Полученные данные:', data)
        return JsonResponse({'message': 'Данные успешно получены'}, status=200)

    else:
        form = PromoDayForm()
    return render(request, 'food/index.html', {'form': form})
