from django.urls import path
from crud_app import views
app_name = 'crud_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.student_forms, name='form'),
    path('student_info/<int:id>/', views.student_info,name='student_info'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.student_delete, name='delete'),
]
