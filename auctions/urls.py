from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:item_id>", views.item, name="item"),
    path("newlist", views.newlist, name="newlist"),
    path("savelist", views.savelist, name="savelist")
    
]
