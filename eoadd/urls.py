from django.urls import path
from eoadd.views import home
from eoadd import views as eoadd_views

urlpatterns = [
    path('',home),
    path("cal", eoadd_views.cal, name="cal11"),
    path("fact", eoadd_views.factorial, name="fact11")
]