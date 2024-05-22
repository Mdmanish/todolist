from django.urls import path

from .views import HomeView

urlpatterns = [
    # path('/login', views.login, name='login'),
    # path('/register', views.register, name='register'),
    path('', HomeView.as_view(), name='home'),
    path('<int:todo_id>/', HomeView.as_view(), name='home'),
    # path('', HomeView.as_view(), name='add'),
    # path('complete/<todo_id>', HomeView.as_view(), name='complete'),
    # path('deletecomplete/', HomeView.as_view(), name='deletecomplete'),
    # path('deleteall/', HomeView.as_view(), name='deleteall'),
]
