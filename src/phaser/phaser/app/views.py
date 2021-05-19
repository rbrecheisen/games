from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def phaser(request):
    return render(request, 'phaser.html')


def tankbatallion(request):
    return render(request, 'tankbatallion.html')
