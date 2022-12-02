from django.contrib import admin
from django.urls import path
from .views import AdminDashboardCreate,AdminDashboardDelete,AdminDashboardList,AdminDashboardUpdate,\
    JobsDashboardCreate,JobsDashboardDelete,JobsDashboardList,JobsDashboardUpdate,CompanyDashboardList,\
        JobsOneDashboardList,PaymentCreate,JobseekerDashboardList


urlpatterns = [
    path('admindashboard/create/', AdminDashboardCreate.as_view(), name="admindashboard_create"),
    path('payment/create/', PaymentCreate.as_view(), name="payment"),
    path('paymentverify/list/', JobseekerDashboardList.as_view(), name="paymentverify"),
    path('admindashboard/list/', AdminDashboardList.as_view(), name='admindashboard_list'),
    path('admindashboard/update/<str:pk>/', AdminDashboardUpdate.as_view(), name='admindashboard_update'),
    path('admindashboard/delete/<str:pk>/', AdminDashboardDelete.as_view(),name="admindashboard_delete"),
    path('jobdashboard/create/', JobsDashboardCreate.as_view(), name="jobdashboard_create"),
    path('jobdashboard/list/', JobsDashboardList.as_view(), name='jobdashboard_list'),
    path('jobdashboard/update/<str:pk>/', JobsDashboardUpdate.as_view(), name='jobdashboard_update'),
    path('jobdashboard/delete/<str:pk>/', JobsDashboardDelete.as_view(),name="jobdashboard_delete"),
    path('companydashboard/list/', CompanyDashboardList.as_view(), name='companydashboard_list'),
    path('jobonedashboard/list/', JobsOneDashboardList.as_view(), name='jobonedashboard_list'),

]