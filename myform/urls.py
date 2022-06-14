from django.urls import path
from myform import views

urlpatterns =[
    path('',views.form_page,name='form'),
]