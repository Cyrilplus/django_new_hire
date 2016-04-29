import datetime
import json
import re

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
    action = request.POST['action']
    pattern = re.compile(r'data\[(\d+)\]\[(.+)\]')
    if action == 'create':
        new_row = Rows()
        for key in request.POST:
            match = re.match(pattern, key)
            if match is not None:
                new_row.set_value(match.group(2), request.POST[key])
        new_row.save()
        row_dictionary = {
            'DT_RowId': new_row.id,
            'new_hire_id': new_row.new_hire_id,
            'new_hire_name': new_row.new_hire_name,
            'manager_id': new_row.manager_id,
            'manager_name': new_row.manager_name,
            'onboard_time': new_row.onboard_time,
            'created_time': new_row.created_time.strftime('%Y-%m-%d'),
            'age': 0,
            'status': new_row.status,
        }

        return HttpResponse(json.dumps({'data': [row_dictionary, ]}), content_type='application/json')
    elif action == 'edit':
        row_id = 0;
        edit_row = None
        for key in request.POST:
            match = re.match(pattern, key)
            if match is not None:
                if row_id == 0:
                    row_id = int(match.group(1))
                    edit_row = Rows.objects.get(id=row_id)
                print "key: " + match.group(2) + ' value:' + request.POST[key]
                edit_row.set_value(match.group(2), request.POST[key])
        if edit_row is not None:
            edit_row.save()
            row_dictionary = {
                'DT_RowId': edit_row.id,
                'new_hire_id': edit_row.new_hire_id,
                'new_hire_name': edit_row.new_hire_name,
                'manager_id': edit_row.manager_id,
                'manager_name': edit_row.manager_name,
                'onboard_time': edit_row.onboard_time if not isinstance(edit_row.onboard_time,
                                                                    datetime.datetime) else edit_row.onboard_time.strftime(
                    '%Y-%m-%d'),
                'created_time': edit_row.created_time.strftime('%Y-%m-%d'),
                'age': 0,
                'status': edit_row.status,
            }
            return HttpResponse(json.dumps({'data': [row_dictionary, ]}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'data': None}), content_type='application/json')
    elif action == 'remove':
        for key in request.POST:
            match = re.match(pattern, key)
            if match is not None:
                Rows.objects.get(id=match.group(1)).delete()
                return HttpResponse(json.dumps({'data': None}), content_type='application/json')
        return HttpResponse(json.dumps({'data': None}), content_type='application/json')
    else:
        pass
    return get_new_hire(request)
