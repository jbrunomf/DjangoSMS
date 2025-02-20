from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.BrandListView.as_view(), name='brand_list'),
    path('create/', views.BrandCreateView.as_view(), name='brand_create'),
    path('update/<int:pk>/', views.BrandUpdateView.as_view(), name='brand_update'),
    path('detail/<int:pk>/', views.BrandDetailView.as_view(), name='brand_detail'),
    path('delete/<int:pk>/', views.BrandDeleteView.as_view(), name='brand_delete'),
]
