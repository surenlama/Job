from django.shortcuts import render
from django.contrib import messages
# from .filters import BillFilter
# Create your views here.
from jobapp.models import Category,Job
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView
from .forms import CategoryForm,JobForm
# from django_filters.views import FilterView
from django.core.mail import EmailMessage



class CategoryCreate(CreateView):
    form_class = CategoryForm
    template_name = "category.html"
    success_url = '/category/create/'
    

class CategoryList(ListView):
    model = Category
    template_name = "category.html"
    success_url = '/category/create/'
    context_object_name = "category_list"


class CategoryListOne(ListView):
    model = Category
    template_name = "category.html"
    success_url = '/categoryone/update/'
    context_object_name = "category_list"


class CategoryUpdate(UpdateView):
    # queryset = Patient.objects.all()(yo gardani huncha ya model rakhda ni hunhca)
    model = Category
    form_class = CategoryForm
    template_name = "category.html"
    success_url = '/admindashboard/list/'    


class CategoryDelete(DeleteView):
    # queryset = Patient.objects.all()(yo gardani huncha ya model rakhda ni hunhca)
    model = Category
    template_name = "categorydelete.html"
    success_url = '/admindashboard/list/'  
    

class JobCreate(CreateView):
    form_class = JobForm
    template_name = "job.html"
    success_url = '/job/create/'
    

class JobList(ListView):
    model = Job
    template_name = "admindashboard.html"
    success_url = '/admindashboard/list'
    context_object_name = "job_list"


class JobUpdate(UpdateView):
    # queryset = Patient.objects.all()(yo gardani huncha ya model rakhda ni hunhca)
    model = Job
    form_class = JobForm
    template_name = "job.html"
    success_url = '/admindashboard/list/'    


class JobDelete(DeleteView):
    # queryset = Patient.objects.all()(yo gardani huncha ya model rakhda ni hunhca)
    model = Job
    template_name = "jobdelete.html"
    success_url = '/admindashboard/list/'    
