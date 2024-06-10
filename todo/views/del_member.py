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
def del_member(request, group_id) -> HttpResponse:
    """
    创建团队，并把创建者设置为管理员
    """

    # Only staffers can add lists, regardless of TODO_STAFF_USER setting.
    # if not request.user.is_staff:
    #     raise PermissionDenied

    if request.POST:
        # User对象
        manager = request.user
        # groupname = request.POST.get('groupname')
        group = Group.objects.get(id = group_id)
        member_id = request.POST.get('member_id')
        print(member_id)
        try:
            member = User.objects.get(id = member_id)
        except:
            messages.info(request, '用户ID不存在')
            return redirect(reverse("todo:list_groups"))
            
        if manager_checker(manager, group):
            # 有权限添加人
            # membername = request.POST.get('member')
            # member = User.objects.get(username = membername)
            # member.group.add(group)
            
            if member not in group.user_set.all():
                messages.info(request, f'用户 {member.username} 不在团队 {group.name} 中！')
                return redirect(reverse("todo:list_groups"))
            
            try:
                group.user_set.remove(member)
                messages.success(request, f'成功从团队 {group.name} 移除用户 {member.username} ！')
            except:
                messages.info(request, f'用户 {member.username} 已在该组中！')
                return redirect(reverse("todo:list_groups"))
                
        else:
            messages.info(request, '移除用户失败！')
            return redirect(reverse("todo:list_groups"))
            
            # raise PermissionDenied
        if member is None:
            messages.info(request, '用户ID不存在')
            
        
        return redirect(reverse("todo:list_groups"))

    # context = {"form": form}

    # return render(request, "todo/add_list.html", context)
