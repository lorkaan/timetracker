from django.urls import path
from . import views

urlpatterns = [
    path("", views.timer_view, name="timer_view"),
    path("toggle/", views.toggle_timer, name="toggle_timer"),
    path("history/", views.history_view, name="history_view"),
]
