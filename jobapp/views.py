from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from jobapp.models import Category,Job,CVUpload
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView
from .forms import CategoryForm,JobForm,JobApplyform
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model


User = get_user_model()



class JobApplyCreate(CreateView):
    form_class = JobApplyform
    template_name = "applycreate.html"
    success_url = '/jobapply/create/'

    def get(self, request):
        fm = JobApplyform()
        userobject = User.objects.get(id=request.user.id)
        dashboard_object = userobject.dashuser.all()
        for i in dashboard_object: 
            if i.apply_attempt==0:
                    print('true')
                    messages.success(request, "Your Account Created Succesully, to Verify your Account Check your Email.")
                    return render(request, 'messag.html')
            else:
                pass
        return render(request, 'applycreate.html', {'form':fm})

    def post(self, request, *args, **kwargs):
        # self.object = None
        # ids = request.POST['send_to']

        userobject = User.objects.get(id=request.user.id)
        dashboard_object = userobject.dashuser.all()
        
        for i in dashboard_object:  
            i.apply_attempt-=1
            i.user=userobject
            i.save()
        name = request.POST['name']
        cv = request.FILES['cv']
        job = request.POST['job']
        job = Job.objects.get(id=job)

        if "cv" in request.FILES:
                CVUpload.objects.create(user=request.user,name=name,job=job,cv=cv)    
        else:
                pass 

  
        # fm = JobApplyform(request.POST)
        # print('form',fm)
        # print('kahbjb')
        # if fm.is_valid():
        #     print('hello')
        #     new_user = fm.save()
        #     new_user.user = request.user
        #     new_user.save()
        #     print('hi')

        # if "payment_screenshot" in request.FILES:
        #     print(request.FILES['payment_screenshot'])
        #     send_email_after_payment(userobject.email,userobject.username)
        #     messages.success(request, "Please check your email for transaction.")          
        #     return HttpResponseRedirect('/jobdashboard/create/')  
        # else:
        #     messages.success(request, "Please put your payment screenshot.")   
        #     print('sorry')             
        # course_object[0].save()  
        return HttpResponseRedirect('/jobapply/create/')  
        


class JobApplyList(ListView):
    model = CVUpload
    template_name = "apply.html"
    success_url = '/jobapply/list/'
    # context_object_name = "jobapply_list"

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data()
        b=CVUpload.objects.exclude(job__category__name="freelancer")
        c=b.filter(job__post_by=self.request.user)
        print('c',c)
        context['jobapply_list']=c

        return context


class FreelancerApplyList(ListView):
    model = CVUpload
    template_name = "freelancer.html"
    success_url = '/freelancerapply/list/'
    context_object_name = "freelancerapply_list"

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data()
        a=CVUpload.objects.filter(job__category__name="freelancer",job__post_by=self.request.user)
        context['freelancer_list']=a
        return context

class CategoryCreate(CreateView):
    form_class = CategoryForm
    template_name = "category.html"
    success_url = '/category/create/'
    

class CategoryList(ListView):
    model = Category
    template_name = "admindashboard.html"
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
