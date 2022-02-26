from django.contrib import admin
from django.urls import path, include
from .views import CarsDetailView, UsersView  # CommentsListView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cars', CarsDetailView)
router.register('users', UsersView)

app_name = 'car'

urlpatterns = []

urlpatterns += router.urls