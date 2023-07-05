from django.shortcuts import render

def protocols_list(request):
    return render(request, 'protocols/protocolslist.html')
