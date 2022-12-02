from django.shortcuts import render
from django.contrib import messages
from dashboardapp.models import Dashboard
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView
from .forms import AdminDashboardForm,JobDashboardForm,JobDashboard1Form
# from django_filters.views import FilterView
from django.core.mail import EmailMessage
from jobapp.models import Category,Job

from django.shortcuts import render, HttpResponse,HttpResponseRedirect




from django.core.mail import send_mail

from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()



def send_email_after_payment(email,username):
    subject = "Transaction Alert"
    message = f'Dear{username} Your account has benn credited by 300, please check it.Thank you.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)


class AdminDashboardCreate(CreateView):
    form_class = AdminDashboardForm
    # form_classes = {'admin': AdminDashboardForm,
    #                 'category': CategoryForm}
    template_name = "admindashboard.html"
    success_url = '/admindashboard/create/'

class PaymentCreate(CreateView):
    form_class = AdminDashboardForm
    template_name = "payment.html"
    success_url = '/payment/create/'

class AdminDashboardList(ListView):
    model = Category
    template_name = "admindashboard.html"
    success_url = '/admindashboard/list'
    context_object_name = "category_list"

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data()
        context['jobs']=Job.objects.all()
        print(context)
        return context
 

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
    success_url = '/jobdashboard/create/'

    def get(self, request):
        fm = JobDashboardForm()
        return render(request, 'jobseekerdashboard.html', {'form':fm})

    def post(self, request):
        fm = JobDashboardForm(request.POST)
        if fm.is_valid():
            new_user = fm.save()
            print(new_user)
            screen_object = fm.cleaned_data['payment_screenshot']
            print(screen_object)
            ids=fm.cleaned_data['send_to'].id
            userobject = User.objects.get(id=ids)
            if screen_object:      
                send_email_after_payment(userobject.email,userobject.username)
                messages.success(request, "Please check your email fortransaction.")          
                return render(request, 'jobseekerdashboard.html', {'form':fm})        

            else:
                messages.success(request, "Please put your payment screenshot.")                
            # course_object[0].save()          
            return render(request, 'jobseekerdashboard.html', {'form':fm})        


        return render(request, 'jobseekerdashboard.html', {'form':fm})        



class JobsDashboardList(ListView):
    model = Dashboard
    template_name = "jobseekerdashboard.html"
    success_url = '/dashboard/list/'
    context_object_name = "dashboard_list"


class JobseekerDashboardList(ListView):
    model = Dashboard
    template_name = "paymentverify.html"
    success_url = '/paymentverify/list/'
    context_object_name = "paymentverify_list"

class JobsDashboardUpdate(UpdateView):
    model = Dashboard
    form_class = JobDashboard1Form
    template_name = "jobseekerdashboard.html"
    success_url = '/paymentverify/list/'


class JobsDashboardDelete(DeleteView):
    model = Dashboard
    template_name = "jobseekerdashboard.html"
    success_url = '/dashboard/list/'      

class JobsOneDashboardList(ListView):
    model = Dashboard
    template_name = "jobdashboard.html"
    success_url = '/jobonedashboard/list/'
    context_object_name = "dashboard_list"

class CompanyDashboardList(ListView):
    model = Dashboard
    template_name = "companydashboard.html"
    success_url = '/companydashboard/list/'
    context_object_name = "dashboard_list"
