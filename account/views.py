from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import CreateView,ListView,View,DetailView,UpdateView
from .forms import SignUpForm, UserAuthentiationForm,CompanySignupForm,AdminSignupForm,ContactForm
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.core.mail import send_mail
from django.views.generic.base import TemplateView
import uuid
import tempfile
from jobapp.models import Category
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from jobproject.func import render_to_pdf
from .models import Skills,Project,Education,Experiences,Course,TermsAndCondition,Blog,Contact
from dashboardapp.models import Dashboard,Quotes,Dommy
from account.task import delete_unpaiduser,quotesgenerate
import  random
import time
from jobapp.models import Job
from jobapp.forms import JobForm
import datetime
# from datetime import datetime, timedelta
from django.core.paginator import Paginator


User = get_user_model()



def send_email_after_registration(email,token):
    subject = "Verify Email"
    message = f'Hi Click on the link to verify your account http://127.0.0.1:8000/account/acount-verify/{token}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)

def send_email_after_payment(email,username):
    subject = "Transaction Alert"
    message = f'Dear{username} Your account has benn credited by 300, please check it.Thank you.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
#verification
def account_verify(request, token):
    usr = User.objects.filter(token=token).first()
    usr.verify = True
    usr.save()
    messages.success(request, "Your account has been verified, you can login")
    return redirect('/account/login/')

def home(request):
    job_object = Job.objects.all()
    print('jobobject',job_object)
    return render(request,'index.html',{'jobobj':job_object})

class JobSeekerCreate(CreateView):
    form_class = AdminSignupForm
    template_name = "jobsignup.html"
    success_url = '/jobseekercreate/'

    def get(self, request):
        fm = AdminSignupForm()
        return render(request, 'jobsignup.html', {'form':fm})

    def post(self, request):
        fm = AdminSignupForm(request.POST,request.FILES)
        if fm.is_valid():
            new_user = fm.save()
            print(new_user)
            uid = uuid.uuid4()
            new_user.token = uid
            new_user.user_type = "Job_seeker"
            print(new_user)
            new_user.verify = True
            new_user.is_staff=True
            new_user.is_active=True
            current_date = datetime.datetime.now()
            new_date = current_date+datetime.timedelta(days=15)
            newss_date = new_date.date()
            new_user.paymentend_date=newss_date
            new_user.create_date = datetime.datetime.now().date()
            print(fm.cleaned_data['image'])
            new_user.image = fm.cleaned_data['image']
            new_user.save()
            ids = new_user.id
            # print(ids)
            # send_email_after_registration(new_user.email,uid)
            messages.success(request, "Your Account Created Succesully.")
            # return HttpResponseRedirect(f'/account/pdfgenerator/{ids}')  

        return render(request, 'jobsignup.html', {'form':fm})


class JobSeekerSignUp(CreateView):
    form_class = SignUpForm
    template_name = "jobsignup.html"
    success_url = '/account/jobsignup/'

    # def get(self, request):
    #     fm = SignUpForm()
    #     return render(request, 'signup.html', {'form':fm})
    def post(self, request):
        fm = SignUpForm(request.POST)
        print(fm)
        if fm.is_valid():
            new_user = fm.save()
            print(new_user)
            uid = uuid.uuid4()
            new_user.token = uid
            new_user.user_type = "Job_seeker"
            print(new_user)
            current_date = datetime.datetime.now()
            new_date = current_date+datetime.timedelta(days=15)
            newss_date = new_date.date()
            new_user.paymentend_date=newss_date
            new_user.create_date = datetime.datetime.now().date()
            new_user.save()
            ids = new_user.id
            print(ids)
            send_email_after_registration(new_user.email,uid)
            messages.success(request, "Your Account Created Succesully, to Verify your Account Check your Email.")
            return HttpResponseRedirect(f'/account/pdfgenerator/{ids}')  

        return render(request, 'jobsignup.html', {'form':fm})

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "signup.html"
    success_url = '/account/login/'

    # def get(self, request):
    #     fm = SignUpForm()
    #     return render(request, 'signup.html', {'form':fm})

    def post(self, request):
        fm = SignUpForm(request.POST,request.FILES)
        if fm.is_valid():
            new_user = fm.save()
            uid = uuid.uuid4()
            new_user.token = uid
            new_user.user_type = "Job_seeker"
            current_date = datetime.datetime.now()
            new_date = current_date+datetime.timedelta(days=15)
            newss_date = new_date.date()
            new_user.paymentend_date=newss_date
            new_user.create_date = datetime.datetime.now().date()
            # print(request.FILES['image'])
            new_user.image = request.POST['image']
            new_user.save()

            ids = new_user.id

                
            send_email_after_registration(new_user.email,uid)
            messages.success(request, "Your Account Created Succesully, to Verify your Account Check your Email.")
            # return HttpResponseRedirect(f'/account/pdfgenerator/{ids}')  
            #   
    
        return render(request, 'login.html', {'form':fm})


class AdminSignUp(CreateView):
    form_class = AdminSignupForm
    template_name = "signup.html"
    success_url = '/account/login/'

    # def get(self, request):
    #     fm = SignUpForm()
    #     return render(request, 'signup.html', {'form':fm})

    def post(self, request):
        fm = AdminSignupForm(request.POST,request.FILES)
        print(fm)
        if fm.is_valid():
            new_user = fm.save()
            print(new_user)
            uid = uuid.uuid4()
            new_user.token = uid
            new_user.user_type = "Admin"
            if "image" in request.FILES:
                new_user.image = request.FILES['image']
            print(new_user)
            new_user.save()
            send_email_after_registration(new_user.email,uid)
            messages.success(request, "Your Account Created Succesully, to Verify your Account Check your Email.")

        return render(request, 'login.html', {'form':fm})


class Signin(View):
    template_name = 'login.html'
    form_class = UserAuthentiationForm
    
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        if request.method=="POST":
            fm = UserAuthentiationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                # add.delay()
                if user is not None:
                    if user.verify:
                        if user.user_type =="Job_seeker":
                            login(request,user)
                            return HttpResponseRedirect('/admindashboard/list/')  
                        elif user.user_type == "Company":
                            login(request,user)
                            return HttpResponseRedirect('/admindashboard/list/')  
                            # return HttpResponseRedirect('/companydashboard/list/')  
                    
                        elif user.user_type == "Admin":
                            login(request,user)
                            return HttpResponseRedirect('/admindashboard/list/')  
                        else:
                            pass        
                  
                    else:
                        messages.info(request,"Your account is not verified, please check your email and verify your account.")
                        return render(request,self.template_name)    
       
            else:

                fm = UserAuthentiationForm()
                messages.info(request,"Invalid login credential.")
            return render(request,self.template_name,{'form':fm})    
                        


class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')


def changepass(request):
    if request.method=="POST":
        current=request.POST['currentpass']
        change=request.POST['changepass']
        confirm=request.POST['confirmpass']
        usr=User.objects.get(id=request.user.id)
        b=usr.username
        v=usr.check_password(current)
        if v:
            if change==confirm:               
                usr.set_password(confirm)
                usr.save()
                us=User.objects.get(username=b)
                login(request,us)
                msg="Sucessfully changed password"
            else:
                msg="Password doesn't match"    
        else: 
            msg="Incorrect current password"   
        return render(request,'changepassword.html',{'msg':msg})
    return render(request,'changepassword.html')   

#Company
class CompanyCreate(CreateView):
    form_class = CompanySignupForm
    template_name = "companysignup.html"
    success_url = '/account/companycreate/'

    def get(self, request):
        fm = CompanySignupForm()
        return render(request, 'companysignup.html', {'form':fm})

    def post(self, request):
        fm = CompanySignupForm(request.POST,request.FILES)
        if fm.is_valid():
            company_user = fm.save()
            user = User.objects.create_user(username=fm.cleaned_data['name'],email=fm.cleaned_data['email'],password=fm.cleaned_data['password1'])
            user.is_staff=True  
            user.is_active=True
            user.user_type = "Company"
            user.verify=True
            user.image = request.FILES['image']
            uid = uuid.uuid4()
            user.token = uid
            current_date = datetime.datetime.now()
            new_date = current_date+datetime.timedelta(days=15)
            newss_date = new_date.date()
            user.paymentend_date=newss_date
            user.create_date = datetime.datetime.now().date()
            user.save()          
            company_user.image=request.FILES['image']
            # print(new_user)
            company_user.save()
            # send_email_after_registration(user.email,uid)
            messages.success(request, "Your Account Created Succesully.")

        return render(request, 'companysignup.html', {'form':fm})


#Company
class CompanySignUp(CreateView):
    form_class = CompanySignupForm
    template_name = "signup.html"
    success_url = '/account/companysignup/'

    # def get(self, request):
    #     fm = CompanySignupForm()
    #     return render(request, 'signup.html', {'form':fm})

    def post(self, request):
        fm = CompanySignupForm(request.POST,request.FILES)
        if fm.is_valid():
            company_user = fm.save()
            user = User.objects.create_user(username=fm.cleaned_data['name'],email=fm.cleaned_data['email'],password=fm.cleaned_data['password1'])
            user.is_staff=True  
            user.is_active=True
            user.user_type = "Company"
            user.location = fm.cleaned_data['location']
            if "image" in request.FILES:
                user.image = request.FILES['image']
            uid = uuid.uuid4()
            user.token = uid
            current_date = datetime.datetime.now()
            new_date = current_date+datetime.timedelta(days=15)
            newss_date = new_date.date()
            user.paymentend_date=newss_date
            user.create_date = datetime.datetime.now().date()
            user.save()          
            # print(new_user)
            company_user.save()
            send_email_after_registration(user.email,uid)
            messages.success(request, "Your Account Created Succesully, to Verify your Account Check your Email.")

        return render(request, 'signup.html', {'form':fm})


class Indexx(ListView):
    model = Category
    template_name = "index.html"
    success_url = '/category/list/'
    context_object_name = "category_list"

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data()
        # lst=[]
        # user_object = Quotes.objects.all()
        # for i in user_object:
        #     lst.append(i.id)
        # ranvalue = random.randint(min(lst),max(lst))
        random_val = Dommy.objects.all()
        print(random_val)
        print(random_val[0].number)
        randomobject = Quotes.objects.get(id=random_val[0].number)
        if 'q' in self.request.GET:
            q=self.request.GET['q']
            data = Category.objects.filter(main__category_type="Freelancing Work",name__icontains=q)
        else:
            data = Category.objects.filter(main__category_type="Freelancing Work")
            print(data)
        onsite = Category.objects.exclude(main__category_type="Freelancing Work")
        context=super().get_context_data()
        context['categoryonsite_list']=onsite

        context['category_list']=data
        context['quotes']=randomobject
        job_obj = Job.objects.all()[:3]
        context['jobobj']=job_obj
        digital_obj = Category.objects.filter(category_type="Digital Work")
        context['digital']=digital_obj
        field_obj = Category.objects.filter(category_type="Field Work")
        context['field']=field_obj
        return context

class JobListing(ListView):
    model = Job
    form_class=JobForm
    template_name = "job_listing.html"
    success_url = '/account/findjob/'
    context_object_name = "job_list"

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data()
        category_obj = Category.objects.all()
        job_obj = Job.objects.all()
        # filter for job type
        print(self.kwargs['pk'])
        print(type(self.kwargs['pk']))
        today = datetime.datetime.now().date()
        print(today)
        if self.kwargs['pk'] == "-1":
            jobfiltobj = Job.objects.filter(job_type="Full Time")
            context['job_filter']=jobfiltobj

        elif self.kwargs['pk'] == "-2":  
            jobfiltobj = Job.objects.filter(job_type="Part Time")
            context['job_filter']=jobfiltobj

        elif self.kwargs['pk'] == "-3":  
            jobfiltobj = Job.objects.filter(job_type="Remote")
            context['job_filter']=jobfiltobj

        elif self.kwargs['pk'] == "-4":  
            jobfiltobj = Job.objects.filter(job_type="Freelancing")
            context['job_filter']=jobfiltobj

        elif self.kwargs['pk'] == "-10": 
            jobfiltobj = Job.objects.filter(posted_date=today)
            context['job_filter']=jobfiltobj


        elif self.kwargs['pk'] == "-20": 
            future_date_before_2days = today - \
                                    datetime.timedelta(days = 2)
            jobfiltobj = Job.objects.filter(posted_date=future_date_before_2days)
            context['job_filter']=jobfiltobj

        elif self.kwargs['pk'] == "-30": 
            future_date_before_3days = today - \
                                    datetime.timedelta(days = 3)
            jobfiltobj = Job.objects.filter(posted_date=future_date_before_3days)
            context['job_filter']=jobfiltobj

        elif self.kwargs['pk'] == "-50": 
            future_date_before_5days = today - \
                                    datetime.timedelta(days = 5)
            jobfiltobj = Job.objects.filter(posted_date=future_date_before_5days)
            context['job_filter']=jobfiltobj

        elif self.kwargs['pk'] == "-100": 
            future_date_before_10days = today - \
                                    datetime.timedelta(days = 10)
            jobfiltobj = Job.objects.filter(posted_date=future_date_before_10days)
            context['job_filter']=jobfiltobj

        elif self.kwargs['pk'] == "-55": 
            objs=Job.objects.all()
            paginator=Paginator(objs,4)
            page_number=self.request.GET.get('page')
            servicedata = paginator.get_page(page_number)
            print('servicedata',servicedata)

            context['job_filter']=servicedata

        else:
            pass


        #filter for job of category
        cate= Category.objects.filter(id=self.kwargs['pk'])
        print('cate',cate)
        if cate:
            category_filt = Category.objects.get(id=self.kwargs['pk'])
            jobfiltobj = Job.objects.filter(category=category_filt)
            if len(jobfiltobj)<0:
                context['message']="No jobs found"
            else:
                context['job_filter']=jobfiltobj
        else:
            messages.info(self.request,"Doesnot have data.")
        # paginator=Paginator(data,4)
        # page_number=self.request.GET.get('page')
        # servicedata = paginator.get_page(page_number)
        #filter forjob location 
        jobfiltobj = Job.objects.filter(id=self.kwargs['pk'])
        if jobfiltobj:
            context['job_filter']=jobfiltobj

        context['category_all']=category_obj
        context['job_list']=job_obj
        # context['job_filter']=jobfiltobj
        return context

class Jobdetail(UpdateView):
    model = Job
    form_class=JobForm
    template_name = "job_details.html"

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data()
        job_obj = Job.objects.get(id=self.kwargs['pk'])
        context['job_list']=job_obj

        return context    

class About(TemplateView):
    template_name = "about.html"

class Contact(CreateView):
    form_class = ContactForm
    template_name = "contact.html"
    success_url = '/account/contact/'

    

class TermsCondition(ListView):
    model = Category
    template_name = "terms.html"
    def get(self, request):
        terms_object = TermsAndCondition.objects.all()
        print(terms_object)
        data = {
            "object": terms_object,
            "base_url": request.build_absolute_uri(),

        }
        a = render_to_pdf(self.template_name, context=data)
        response = HttpResponse(content_type="application/pdf")
        response[
            "Content-Disposition"
        ] = f"attachment; filename=terms.pdf"
        response["Content-Transfer-Encoding"] = "binary"

        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(a)
            output.flush()
            output = open(output.name, "rb")
            response.write(output.read())
            return response
  

class UserPDFView(DetailView):
    template_name = "cvv.html"
    model = User

    def get(self, request,pk):
        user_object = User.objects.get(id=self.get_object().id)
        experience = user_object.experience.all()
        education = user_object.education.all()
        skill = user_object.skill.all()
        course = user_object.course.all()
        project = user_object.project.all()
        print(experience)
        data = {
            "object": user_object,
            "experience": experience,
            "education": education,
            "skill":skill,
            "course":course,
            "project":project,
            "base_url": request.build_absolute_uri(),
        }
        a = render_to_pdf(self.template_name, context=data)
        response = HttpResponse(content_type="application/pdf")
        response[
            "Content-Disposition"
        ] = f"attachment; filename=CV_{user_object.id}.pdf"
        response["Content-Transfer-Encoding"] = "binary"

        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(a)
            output.flush()
            output = open(output.name, "rb")
            response.write(output.read())
            return response



class ViewCVList(ListView):
    model = User
    template_name = "cv.html"
    success_url = '/viewcv/list'
    context_object_name = "cv_list"

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data()
        user_object = User.objects.get(id=self.request.user.id)
        experience = user_object.experience.all()
        education = user_object.education.all()
        skill = user_object.skill.all()
        course = user_object.course.all()
        project = user_object.project.all()        
        context['object']=user_object
        context['experience']=experience
        context['education']=education
        context['skill']=skill
        context['course']=course
        context['project']=project
        return context


class BlogList(ListView):
    model = Blog
    template_name = "blog.html"
    success_url = '/account/blog'
    context_object_name = "blog_list"

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data()
        blog_object = Blog.objects.all().order_by('-id')[:2]
        print(blog_object)
        context['blog_obj']=blog_object
        return context
