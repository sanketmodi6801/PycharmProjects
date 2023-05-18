from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index', views.index),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path('home', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('checkout', views.checkout),
    path('tracker', views.tracker),
    path("tracked", views.tracked),
    path("Logout", views.Logout),
]
