from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import CreateView,ListView,View
from .forms import SignUpForm, UserAuthentiationForm,CompanySignupForm,AdminSignupForm
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.core.mail import send_mail
from django.views.generic.base import TemplateView
import uuid
from jobapp.models import Category
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()



def send_email_after_registration(email,token):
    subject = "Verify Email"
    message = f'Hi Click on the link to verify your account http://127.0.0.1:8000/account/acount-verify/{token}'
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
    return render(request,'base.html')

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "signup.html"
    success_url = '/account/login/'

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
            new_user.save()
            send_email_after_registration(new_user.email,uid)
            messages.success(request, "Your Account Created Succesully, to Verify your Account Check your Email.")

        return render(request, 'login.html', {'form':fm})


class AdminSignUp(CreateView):
    form_class = AdminSignupForm
    template_name = "signup.html"
    success_url = '/account/login/'

    # def get(self, request):
    #     fm = SignUpForm()
    #     return render(request, 'signup.html', {'form':fm})

    def post(self, request):
        fm = AdminSignupForm(request.POST)
        print(fm)
        if fm.is_valid():
            new_user = fm.save()
            print(new_user)
            uid = uuid.uuid4()
            new_user.token = uid
            new_user.user_type = "Admin"
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
                if user is not None:
                    if user.verify:
                        if user.user_type =="Job_seeker":
                            login(request,user)
                            return render(request,'jobdashboard.html')
                        elif user.user_type == "Company":
                            login(request,user)
                            return render(request,'companydashboard.html') 
                        elif user.user_type == "Admin":
                            login(request,user)
                            return HttpResponseRedirect('/admindashboard/create/')  
                        else:
                            pass        
                  
                    else:
                        messages.info(request,"Your account is not verified, please check your email and verify your account.")
                        return render(request,self.template_name)    
       
            else:

                fm = UserAuthentiationForm()
                messages.info(request,"Invalid login credential.")
            return render(request,self.template_name,{'form':fm})    
                        

# class SignUpView(TemplateView):
#     template_name = 'signup.html'

#     def get(self, request):
#         context = super().get_context_data(**kwargs)
#         fm = SignUpForm()
#         context['form'] = fm
#         return context

#     def post(self, request):
#         fm = SignUpForm(request.POST)
#         print(fm)
#         if fm.is_valid():
#             fm.save()
#         else:
#             print('not inserteds')
#             fm = SignUpForm()
#         return render(request, self.template_name, {'form': fm})


# def signup(request):
#     if request.method == "POST":
#         fm = SignUpForm(request.POST)
#         if fm.is_valid():
#             # messages.success(request, "Account Created Successfully !!")
#             fm.save()
#         else:
#             fm = SignUpForm()
#             return render(request, 'signup.html', {'form': fm})
#     return HttpResponse(request, 'signup.html', {})
# def clean(self):
#     form_data = self.cleaned_data
#     if form_data['password'] != form_data['password_repeat']:
#         self._errors["password"] = ["Password do not match"] # Will raise a error message
#         del form_data['password']
#     return form_data

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
        return render(request,'changepass.html',{'msg':msg})
    return render(request,'changepass.html')   


#Company
class CompanySignUp(CreateView):
    form_class = CompanySignupForm
    template_name = "signup.html"
    success_url = '/account/login/'

    # def get(self, request):
    #     fm = SignUpForm()
    #     return render(request, 'signup.html', {'form':fm})

    def post(self, request):
        fm = CompanySignupForm(request.POST)
        print(fm)
        if fm.is_valid():
            company_user = fm.save()
            user = User.objects.create_user(username=fm.cleaned_data['name'],email=fm.cleaned_data['email'],password=fm.cleaned_data['password1'])
            user.is_staff=True  
            user.is_active=True
            user.user_type = "Company"
            uid = uuid.uuid4()
            user.token = uid
            user.save()          

            # print(new_user)
            company_user.save()
            send_email_after_registration(user.email,uid)
            messages.success(request, "Your Account Created Succesully, to Verify your Account Check your Email.")

        return render(request, 'login.html', {'form':fm})



    
class Indexx(ListView):
    model = Category
    template_name = "index.html"
    success_url = '/category/list/'
    context_object_name = "category_list"

class FindJob(TemplateView):
    template_name = "job_listing.html"


class About(TemplateView):
    template_name = "about.html"

class Contact(TemplateView):
    template_name = "contact.html"
