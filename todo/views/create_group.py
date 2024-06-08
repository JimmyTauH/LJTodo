from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
import json

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
        groupname = request.POST.get('groupname')
        try:
            group = Group.objects.create(name = groupname)
            ManagerList.objects.create(manager = manager, group = group)
            manager.group.add(group)
            manager.save()
            group.save()
        except:
            return HttpResponse(json.dumps({'result':False}), content_type='application/json')
        
        # context = {"form": form}
        
        return HttpResponse(json.dumps({'result':True}), content_type='application/json')

    # context = {"form": form}

    # return render(request, "todo/add_list.html", context)
