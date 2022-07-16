from django.urls import path
from .views import *

import buildings

urlpatterns = [
    path('', get_manager),
]
