from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied
import json
from django.shortcuts import render, redirect

from todo.models import ManagerList


@login_required
def create_group(request) -> HttpResponse:
    """
    创建团队，并把创建者设置为管理员
    """

    # Only staffers can add lists, regardless of TODO_STAFF_USER setting.
    # if not request.user.is_staff:
    #     raise PermissionDenied

    if request.POST:
        # User对象
        manager = request.user
        # print(request.POST)
        groupname = request.POST.get('groupname')
        # print(groupname)
        try:
            group, created = Group.objects.get_or_create(name = groupname)
            ManagerList.objects.create(manager = manager, group = group)
            manager.groups.add(group)
            manager.save()
            group.save()
        except:
            # return HttpResponse(json.dumps({'result':False}), content_type='application/json')
            raise PermissionDenied
        
        
        # context = {"form": form}
        
    return redirect('todo:list_groups')


    # context = {"form": form}

    # return render(request, "todo/add_list.html", context)
