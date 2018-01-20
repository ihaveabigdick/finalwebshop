from django.shortcuts import render
def main(request):
    '''
    Render the main page
    '''
    context = {'fuck':'我幹破你娘'}
    return render(request, 'main/main.html', context)

def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')
# Create your views here.
