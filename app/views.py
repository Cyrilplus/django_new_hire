import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from models import Rows


# Create your views here.l

def index(request):
    return render(request, 'app/index.html')


@csrf_exempt
def get_new_hire(request):
    objects = Rows.objects.all()
    rows_array = []

    for row in objects:
        row_dictionary = {
            'DT_RowId': row.id,
            'new_hire_id': row.new_hire_id,
            'new_hire_name': row.new_hire_name,
            'manager_id': row.manager_id,
            'manager_name': row.manager_name,
            'onboard_time': row.onboard_time.strftime('%Y-%m-%d'),
            'created_time': row.created_time.strftime('%Y-%m-%d'),
            'age': 0,
            'status': row.status,
        }
        rows_array.append(row_dictionary)

    return HttpResponse(json.dumps({'data': rows_array}), content_type='application/json')


@csrf_exempt
def modified_rows(request):
    for key in request.POST:
        print 'key: ' + key + '  value: ' + request.POST[key]
    # TODO
    # regex
    return HttpResponse('modified')
