"""predictive_ai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index),   
    path('login/',views.login),
    # path('register/',views.register),
    # path('farmer_register/',views.farmer_register), 
    path('user_home/',views.user_home),
    path('expert_home/',views.expert_home),
    path('view_users/',views.view_users),
    path('view_farmers/',views.view_farmers),
    path('manage_crop/',views.manage_crop),
    path('manage_experts/',views.manage_experts),
    path('manage_notification/',views.manage_notification),
    path('view_feedback/',views.view_feedback),
    path('admin_home/',views.admin_home),
    path('view_doubts/',views.view_doubts),
    path('remove_user/<id>',views.remove_user),
    path('remove_farmer/<id>',views.remove_farmer),
    path('send_feedback/',views.send_feedback),
    path('manage_fertilizer/', views.manage_fertilizer),
    path('manage_tips/', views.manage_tips),
    path('expert_notifications/', views.expert_notifications),
    path('viewfarmers/', views.viewfarmers),
    path('viewcrops/', views.viewcrops),
    path('viewcomplaints/', views.viewcomplaints),
    
    
    
    
    path('user_registration', views.user_registration),
    path('farmer_registration', views.farmer_registration),
    path('login_and', views.login_and),
    path('send_complaint', views.send_complaint),
    path('view_complaints', views.view_complaints),
    path('delete_complaint', views.delete_complaint, name='delete_complaint'), 
    path('get_notifications/', views.get_notifications, name='get_notifications'),
    path('add_product/', views.add_product, name='add_product'),
    path('get_products/', views.get_products, name='get_products'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('complete_payment/', views.complete_payment, name='complete_payment'),
    path('view_orders/', views.view_orders, name='complete_payment'),
    path('farmer_sales_order/', views.farmer_sales_order, name='farmer_sales_order'),
    path('mark_as_delivered', views.mark_as_delivered, name='mark_as_delivered'),
    path('send_doubt', views.send_doubt, name='send_doubt'),
    path('fetch_doubts', views.fetch_doubts, name='fetch_doubts'),
    path('view_tips/', views.view_tips, name='view_tips'),
    path('send_farmer_complaint', views.send_farmer_complaint, name='send_farmer_complaint'),
    path('view_farmer_complaints', views.view_farmer_complaints, name='view_farmer_complaints'),
    path('delete_farmer_complaint', views.delete_farmer_complaint, name='delete_farmer_complaint'),
    path('farmer_predict_disease', views.PredictDisease),
]    

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

