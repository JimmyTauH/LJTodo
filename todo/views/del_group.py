from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
import json


from todo.utils import manager_checker


@login_required
def del_group(request, group_id) -> HttpResponse:
    """
    删除团队
    """

    # Only staffers can add lists, regardless of TODO_STAFF_USER setting.
    # if not request.user.is_staff:
    #     raise PermissionDenied

    if request.POST:
        # User对象
        user = request.user
        # groupname = request.POST.get('groupname')
        group = Group.objects.get(id = group_id)
        if manager_checker(user, group):
            # 有权限删除团队
            # 删除用户与团队的隶属关系
            group.user_set.clear()
            group.delete()
            
        else:
            raise PermissionDenied

        # context = {"form": form}
        
        return redirect('todo:list_groups')

    # context = {"form": form}

    # return render(request, "todo/add_list.html", context)
