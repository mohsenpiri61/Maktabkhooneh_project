from django.shortcuts import render

def index_view(request):
    content = {'name': 'Mohsen Piri', 'address': 'Karaj, Alborz Province, Iran ', 'email': 'mopiry@gmail.com', 'phone': '+98 9397266454'}
    return render(request, 'index.html', content)

