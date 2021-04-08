from django.urls import path
from . import views

app_name='app1'

urlpatterns = [
    path('empform/',views.empform),
    path('showemp/',views.showemp),
    path('deleteemp/<int:id>/',views.deleteemp, name = 'delemp'),
    path('updateemp/<int:id>/',views.updateemp, name = 'updateemp')
]