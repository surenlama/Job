from django.shortcuts import render
from django.contrib import messages
from dashboardapp.models import Dashboard,Quotes
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView
from .forms import AdminDashboardForm,JobDashboardForm,JobDashboard1Form
# from django_filters.views import FilterView
from django.core.mail import EmailMessage
from jobapp.models import Category,Job
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse,HttpResponseRedirect




from django.core.mail import send_mail

from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()



def send_email_after_payment(email,username):
    subject = "Transaction Alert"
    message = f'Dear {username} your account has been credited by 300, please check it.Thank you.'
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

        if 'q' in self.request.GET:
            q=self.request.GET['q']
            data = Category.objects.filter(name__icontains=q,post_by=self.request.user)
        elif self.request.user.user_type=="Job_seeker":
            data=Category.objects.all()
        else:
            data = Category.objects.filter(post_by=self.request.user)
        paginator=Paginator(data,4)
        page_number=self.request.GET.get('page')
        servicedata = paginator.get_page(page_number)
        context['category_list']=servicedata


        if 'p' in self.request.GET:
            p=self.request.GET['p']
            bata = Job.objects.filter(name__icontains=p,post_by=self.request.user)
        elif self.request.user.user_type=="Job_seeker":
            bata=Job.objects.all()       
        else:
            bata = Job.objects.filter(post_by=self.request.user)
        paginat=Paginator(bata,4)
        page_number=self.request.GET.get('page')
        mervicedata = paginat.get_page(page_number)
        context['jobs']=mervicedata
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
    # def get_queryset(self):
    #     user = User.objects.filter(user_type="admin")
    #     return user

    def post(self, request, *args, **kwargs):
        # self.object = None
        user = request.POST['user']
        send = request.POST['send_to']
        userobj = User.objects.get(id=user)
        sendobj=User.objects.get(id=send)
        ids = request.POST['send_to']
        userobject = User.objects.get(id=ids)
        if "payment_screenshot" in request.FILES:
            Dashboard.objects.create(payment_screenshot=request.FILES['payment_screenshot'],user=userobj,bank_details=request.POST['bank_details'],send_to=sendobj)
            print(request.FILES['payment_screenshot'])
            send_email_after_payment(userobject.email,userobject.username)
            messages.success(request, "Please check your email for transaction.")          
            return HttpResponseRedirect('/jobdashboard/create/')  
        else:
            messages.success(request, "Please put your payment screenshot.")   
            print('sorry')             
        # course_object[0].save()          
        return render(request, 'jobseekerdashboard.html')        




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

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data()
        if 'unpaid' in self.request.GET:
            data = Dashboard.objects.filter(payment_status="unpaid")

            # data = Category.objects.filter(name__icontains=q,post_by=self.request.user)
        elif 'paid' in self.request.GET:
            data = Dashboard.objects.filter(payment_status="Paid")
        else:
            data = Dashboard.objects.all()   
        # elif self.request.user.user_type=="Job_seeker":
        #     data=Category.objects.all()
        # else:
        #     data = Category.objects.filter(post_by=self.request.user)
        # paginator=Paginator(data,4)
        # page_number=self.request.GET.get('page')
        # servicedata = paginator.get_page(page_number)
        context['paymentverify_list']=data


        return context
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


# class QuotesListView(ListView):
#     model = Quotes
#     template_name = "companydashboard.html"
#     success_url = '/companydashboard/list/'
#     context_object_name = "dashboard_list"

