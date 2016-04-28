from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from models import Rows
from django.views.decorators.csrf import csrf_exempt


# Create your views here.l

def index(request):
    return render(request, 'app/index.html')


@csrf_exempt
def get_new_hire(request):
    result = u'{"data":' + serializers.serialize('json', Rows.objects.all()) + u'}'
    return HttpResponse(result, content_type='application/json')
