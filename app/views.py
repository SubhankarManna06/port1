from django.shortcuts import render, HttpResponse

# Create your views here.
def main(request):
    context={
        'activeMain':'active-tab'
    }
    return render(request, 'main.html', context)

# def index(request):
#     return render(request, 'index.html')

# def about(request):
#     return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')

# def projects(request):
#     return render(request, 'projects.html')

# def skills(request):
#     return render(request, 'skills.html')



def home(request):
    context={
        'activeHome':'active-tab'
    }
    return render(request, 'home.html', context)


def about(request):
    context={
        'activeAbout':'active-tab'
    }
    return render(request, 'about.html', context)


def skills(request):
    context={
        'activeSkills':'active-tab'
    }
    return render(request, 'skills.html', context)


def projects(request):
    context={
        'activeProjects':'active-tab'
    }
    return render(request, 'projects.html', context)


def contact(request):
    context={
        'activeContact':'active-tab'
    }
    return render(request, 'contact.html', context)