import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render

from todo.forms import SearchForm
from todo.models import Task, TaskList
from todo.utils import staff_check

from todo.utils import manager_checker

@login_required
@user_passes_test(staff_check)
def list_groups(request) -> HttpResponse:
    """Homepage view - list of lists a user can view, and ability to add a list.
    """

    user = request.user
    groups = user.groups.all()
    # print(groups)
    groups_manage = [{"id": group.id, "name": group.name} for group in groups if manager_checker(user, group)]
    groups_in = [{"id": group.id, "name": group.name} for group in groups if not manager_checker(user, group)]

    # Make sure user belongs to at least one group.
    context = {
        "groups_manage": groups_manage,
        "groups_in": groups_in,
    }

    return render(request, "todo/list_groups.html", context)
