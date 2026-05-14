from django.shortcuts import render


def rapid_prospect_ai_index(request):
    return render(request, 'official/katek_ai_index.html')


def business_os(request):
    return render(request, 'official/business-os.html')


def education(request):
    return render(request, 'official/education.html')


def enterprise(request):
    return render(request, 'official/enterprise.html')


def ikonik(request):
    return render(request, 'official/ikonik.html')
