from django.urls import path
from .views import *

urlpatterns = [
    path('login/', check_login, name='login'),
    path('home/', home, name='home'),
    path('details/<int:pk>/', lot_details, name="lot_details"),
    path('new/lot', new_lot, name='new_lot'),
    path('new/user', new_user, name='new_user')

]
