from django.shortcuts import render

def index(request):
    # Renders static/index.html as the landing page
    return render(request, 'index.html')

