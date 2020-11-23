from django.urls import path
from crudapp import views #

urlpatterns = [
    path('', views.main, name='main'),
    path('board/', views.board, name='board'), 
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("update/<int:pk>/", views.update, name="update"),
    path("delete/<int:pk>/", views.delete, name="delete"),
]
