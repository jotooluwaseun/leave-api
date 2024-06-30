from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from employee import views

urlpatterns = [
    path('status/', views.status_list),
    path('status/<int:pk>/', views.status_detail),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
