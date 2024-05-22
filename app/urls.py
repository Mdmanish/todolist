from django.urls import path
from django.contrib.auth import views as auth_views

from .views import CreateListView, UpdateDeleteView, RegisterUser, LoginView

urlpatterns = [
    path('signup/', RegisterUser.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('', CreateListView.as_view(), name='create-list-view'),
    path('<int:todo_id>/', UpdateDeleteView.as_view(), name='update-delete-view')
]
