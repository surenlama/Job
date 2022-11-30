from django.contrib import admin
from django.urls import path
from account.views import SignUp,Signin,Logout,changepass,account_verify,home,CompanySignUp,Indexx,\
    FindJob,About,Contact,AdminSignUp
            



urlpatterns = [
    path('signup/', SignUp.as_view(), name="signup"),
    path('adminsignup/', AdminSignUp.as_view(), name="adminsignup"),

    path('login/', Signin.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('changepassword/', changepass,name="changepass"),
    path('acount-verify/<str:token>', account_verify, name="account_verify"),
    path('companysignup/', CompanySignUp.as_view(), name="companysignup"),
    path('home/', home,name="home"),
    path('indexx/', Indexx.as_view(),name="indexx"),
    path('findjob/', FindJob.as_view(),name="findjob"),
    path('about/', About.as_view(),name="about"),
    path('contact/', Contact.as_view(),name="contact"),
]