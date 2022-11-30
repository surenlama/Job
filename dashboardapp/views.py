from django.shortcuts import render
from django.contrib import messages
from dashboardapp.models import Dashboard
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView
from .forms import AdminDashboardForm,JobDashboardForm
# from django_filters.views import FilterView
from django.core.mail import EmailMessage


class AdminDashboardCreate(CreateView):
    form_class = AdminDashboardForm
    template_name = "admindashboard.html"
    success_url = '/admindashboard/create/'



class AdminDashboardList(ListView):
    model = Dashboard
    template_name = "admindashboard.html"
    success_url = '/dashboard/list/'
    context_object_name = "dashboard_list"


class AdminDashboardUpdate(UpdateView):
    model = Dashboard
    form_class = AdminDashboardForm
    template_name = "admindashboard.html"
    success_url = '/dashboard/list/'    


class AdminDashboardDelete(DeleteView):
    model = Dashboard
    template_name = "admindashboard.html"
    success_url = '/dashboard/list/'  


class JobsDashboardCreate(CreateView):
    form_class = JobDashboardForm
    template_name = "jobseekerdashboard.html"
    success_url = '/dashboard/create/'



class JobsDashboardList(ListView):
    model = Dashboard
    template_name = "jobseekerdashboard.html"
    success_url = '/dashboard/list/'
    context_object_name = "dashboard_list"


class JobsDashboardUpdate(UpdateView):
    model = Dashboard
    form_class = AdminDashboardForm
    template_name = "jobseekerdashboard.html"
    success_url = '/dashboard/list/'    


class JobsDashboardDelete(DeleteView):
    model = Dashboard
    template_name = "jobseekerdashboard.html"
    success_url = '/dashboard/list/'      