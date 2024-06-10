from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import TemplateView
from . import views

urlpatterns = (
    [
        path("", views.login, name="login"),
        path("login", views.login, name="login"),
        path("signup", views.signup, name="signup"),
        path("logout", views.logout, name="logout"),
        path("gtdadmin/", admin.site.urls),
        path("admin/", admin.site.urls),
        path("todo/", include("todo.urls", namespace="todo")),
        path("calender/", include("calender.urls", namespace="calender")), # if has calender app
    ]
    # Static media in DEBUG mode:
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
