# Import
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _


# Views
def hello_old(request):
    return HttpResponse("Hello Wolrd !")


def hello(request):
    return render(
        request,
        'users/hello.html',
        {
            'message': _("Hello Wolrd !"),
        }
    )
