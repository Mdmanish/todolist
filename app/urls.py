from django.urls import path
from django.contrib.auth import views as auth_views

from .views import CreateListView, UpdateDeleteView, RegisterUser, LoginView, AddStepView, AddStepDetailedView, CategoryView, CategoryDetailedView, FileView, FileDetailedView

urlpatterns = [
    path('signup/', RegisterUser.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('', CreateListView.as_view(), name='create-list-view'),
    path('<int:todo_id>/', UpdateDeleteView.as_view(), name='update-delete-view'),
    path('addstep/<int:todo_id>/', AddStepView.as_view(), name='add-step'),
    path('addstep/<int:setp_id>/', AddStepDetailedView.as_view(), name='add-step-details'),
    path('category/<int:todo_id>/', CategoryView.as_view(), name='category'),
    path('category/<int:category_id>/', CategoryDetailedView.as_view(), name='category-details'),
    path('file/<int:todo_id>/', FileView.as_view(), name='file'),
    path('file/<int:file_id>/', FileDetailedView.as_view(), name='file-details')
]
