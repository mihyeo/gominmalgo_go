from django.shortcuts import render
import random

def main(request):
    return render(request, 'student1/main.html')
    
    
def random_results(request):
    area = request.GET.get('area')
    
    if area == "경상도":
        place = random
        
        place = random.choice(places)
    return render(request, 'student1/random_results.html', {'area': area, 'place': place})


def first(request):
    return render(request, 'student1/first.html')