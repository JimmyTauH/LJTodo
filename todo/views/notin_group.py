from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
import json

from todo.utils import manager_checker

@login_required
def notin_group(request, group_id) -> HttpResponse:
    """
    创建团队，并把创建者设置为管理员
    """

    # Only staffers can add lists, regardless of TODO_STAFF_USER setting.
    # if not request.user.is_staff:
    #     raise PermissionDenied

    if request.POST:
        # User对象
        # user = request.user
        # groupname = request.POST.get('groupname')
        group = Group.objects.get(id = group_id)
        users_in_group = group.user_set.all()
        # users_all = User.objects.all()
        users_not_in = User.objects.exclude(id__in = users_in_group)

    context={
        'users': users_not_in
    }

    return render(request, "todo/list_groups.html", context)
        
        # return HttpResponse(json.dumps({'users':users_not_in}), content_type='application/json')


