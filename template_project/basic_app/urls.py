from django.urls import path
from basic_app import views

#TEMPLATE TAGGING
app_name = 'basic_app'

#URL PATHS
urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
