# View module. If views not found, import here
from django.http import HttpResponse
from .topics import * 
from .course import *

def index(request):
    return HttpResponse("You have reach the index page. :-)")
