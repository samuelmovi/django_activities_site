from django.urls import path
from . import views

app_name = 'my_site'
urlpatterns = [
    path('', views.base, name='base'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('error/', views.error, name='error'),
    path('<str:lang>/<str:type>/<str:name>/', views.ActivityView.as_view(), name='activity'),
    path('<path:name>/', views.PageView.as_view(), name='page'),
]
