from django.shortcuts import render

# Create your views here.
def home(request):
    cards = [
        {'image': '/static/imgs/key1.jpg', 'title': 'Card 1'},
        {'image': '/static/imgs/key2.jpg', 'title': 'Card 2'},
        {'image': '/static/imgs/key3.jpg', 'title': 'Card 3'},
    ]
    return render(request, 'home.html', {'cards': cards})

def about(request):
    cards = [
        {'image': '/static/imgs/m1.jpg', 'title': 'Card 1'},
        {'image': '/static/imgs/m2.jpg', 'title': 'Card 2'},
        {'image': '/static/imgs/m3.jpg', 'title': 'Card 3'},
    ]
    return render(request, 'about.html', {'cards': cards})

def contact(request):
    cards = [
        {'image': '/static/imgs/lp1.jpg', 'title': 'Card 1'},
        {'image': '/static/imgs/lp2.jpg', 'title': 'Card 2'},
        {'image': '/static/imgs/lp3.jpg', 'title': 'Card 3'},
    ]
    return render(request, 'contact.html', {'cards': cards})