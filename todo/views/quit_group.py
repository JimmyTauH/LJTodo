from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
import json
from django.urls import reverse
from todo.utils import manager_checker

from django.contrib import messages

@login_required
def quit_group(request, group_id) -> HttpResponse:
    """
    创建团队，并把创建者设置为管理员
    """

    # Only staffers can add lists, regardless of TODO_STAFF_USER setting.
    # if not request.user.is_staff:
    #     raise PermissionDenied

    if request.POST:
        # User对象
        user = request.user
        # groupname = request.POST.get('groupname')
        group = Group.objects.get(id = group_id)
        # member_id = request.POST.get('member_id')
        # print(member_id)
        try:
            group.user_set.remove(user)
            messages.success(request, f'退出团队 {group.name} 成功')
        except:
            messages.info(request, '移出失败')
            return redirect(reverse("todo:list_groups"))
        
        return redirect(reverse("todo:list_groups"))

    # context = {"form": form}

    # return render(request, "todo/add_list.html", context)
