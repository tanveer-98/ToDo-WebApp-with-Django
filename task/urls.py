from django.urls import path
from task import views
urlpatterns=[
path('',views.index,name='index'),
path('update_task/<str:pk>',views.updateTask,name='update_task'),
path('delete_task/<str:pk>' , views.deleteTask,name='delete_task')
]
