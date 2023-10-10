from django.urls import path
from .views import *

urlpatterns = [
    path('', ListContent.as_view()),
    path('<int:pk>/', Detailcontent.as_view()),
    path('create', CreateContent.as_view()),
    path('delete/<int:pk>', DeleteContent.as_view()),
]
