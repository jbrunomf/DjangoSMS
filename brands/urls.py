from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.BrandListView.as_view(), name='brand_list'),
    path('create/', views.BrandCreateView.as_view(), name='brand_create'),
    path('update/<int:pk>/', views.BrandUpdateView.as_view(), name='brand_update'),
    path('details/<int:pk>/', views.BrandDetailView.as_view(), name='brand_detail'),
]
