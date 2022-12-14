from django.contrib import admin
from django.urls import path
from jobapp.views import CategoryDelete,CategoryList,CategoryCreate,CategoryUpdate,JobCreate,JobDelete,JobList,JobUpdate,\
    CategoryListOne,JobApplyCreate,JobApplyList,FreelancerApplyList





urlpatterns = [
    path('category/create/', CategoryCreate.as_view(), name="category_create"),
    path('category/list/', CategoryList.as_view(), name='admindashboard_list'),
    path('categoryone/list/', CategoryListOne.as_view(), name='categoryone_list'),
    path('jobapply/create/', JobApplyCreate.as_view(), name='jobapply_create'),
    path('jobapply/list/', JobApplyList.as_view(), name='jobapply_lists'),
    path('freelancerapply/list/', FreelancerApplyList.as_view(), name='freelance_lists'),
    path('category/update/<str:pk>/', CategoryUpdate.as_view(), name='category_update'),
    path('category/delete/<str:pk>/', CategoryDelete.as_view(),name="category_delete"),
    path('job/create/', JobCreate.as_view(), name="job_create"),
    path('job/list/', JobList.as_view(), name='job_list'),
    path('job/update/<str:pk>/', JobUpdate.as_view(), name='job_update'),
    path('job/delete/<str:pk>/', JobDelete.as_view(),name="job_delete"),

]