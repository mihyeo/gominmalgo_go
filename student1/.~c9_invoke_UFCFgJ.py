from django.shortcuts import render


def main(request):
    return render(request, 'student1/main.html')
    
    
def random_results(request):
    area = request.GET.get('area')
    
    if area == "경상도":
        places = ['감자밭', '고구마밭', '성원집']
        
        place = random.choice(places)
    return render(request, 'student1/random_results.html', {'area': area, 'place': place})


def first(request):
    return render(request, 'student1/first.html')