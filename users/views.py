# Import
from django.http import HttpResponse
from django.shortcuts import render


# Views
def hello_old(request):
    return HttpResponse("Hello Wolrd !")


def hello(request):
    return render(
        request,
        'users/hello.html',
        {
            'message': "Hello Wolrd !",
        }
    )
