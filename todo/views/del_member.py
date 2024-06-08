from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
import json

from todo.utils import manager_checker


@login_required
def del_member(request) -> HttpResponse:
    """
    删除团队中的成员，并把创建者设置为管理员
    """

    # Only staffers can add lists, regardless of TODO_STAFF_USER setting.
    # if not request.user.is_staff:
    #     raise PermissionDenied

    if request.POST:
        # User对象
        manager = request.user
        groupname = request.POST.get('groupname')
        group = Group.objects.get(name = groupname)
        if manager_checker(manager, group):
            # 有权限添加人
            membername = request.POST.get('member')
            member = User.objects.get(username = membername)
            group.user_set.remove(member)
        else:
            raise PermissionDenied

        return HttpResponse(json.dumps({'result':True}), content_type='application/json')

