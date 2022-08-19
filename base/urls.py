from django.urls import path, include
from. import views
from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView # new

urlpatterns=[
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='landing.html'),name='landing'),
    path('adminPanel', TemplateView.as_view(template_name='admin.html'),name='adminPanel'),
    path("signup/", views.signup, name="signup"),
    path("signupStaffUser/", views.signupStaffUser, name="signupStaffUser"),
    path('home/',views.home, name='home'),






 


#-----------------------------HM Plus --------------------------------------------

    path('accountDashboard/',views.AccountDashboard, name='Accounts'),
    path('AccountMember/',views.AccountMember, name='Member'),

    path('create_Member/',views.create_Member, name='create_Member'),  
    path('addAccount/',views.addAccount, name='addAccount'),
    path('viewAllAcc/<str:pk>/',views.viewAllAcc, name='viewAllAcc'),
      path('updatePlanType/<str:pk>/',views.updatePlanType, name='updatePlanType'),

    path('addMember/',views.addMember, name='addMember'),
]