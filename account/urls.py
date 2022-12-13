from django.contrib import admin
from django.urls import path
from account.views import SignUp,Signin,Logout,changepass,account_verify,home,CompanySignUp,Indexx,\
    JobListing,About,Contact,AdminSignUp,UserPDFView,JobSeekerSignUp,JobSeekerCreate,CompanyCreate,ViewCVList,\
        Jobdetail,TermsCondition,BlogList



urlpatterns = [
    path('signup/', SignUp.as_view(), name="signup"),
    path('jobsignup/', JobSeekerSignUp.as_view(), name="jobsignup"),
    path('jobseekercreate/', JobSeekerCreate.as_view(), name="jobaccountcreate"),
    path('adminsignup/', AdminSignUp.as_view(), name="adminsignup"),
    path('login/', Signin.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('changepassword/', changepass,name="changepassword"),
    path('acount-verify/<str:token>', account_verify, name="account_verify"),
    path('companysignup/', CompanySignUp.as_view(), name="companysignup"),
    path('companycreate/', CompanyCreate.as_view(), name="companycreate"),
    path('viewcv/list/', ViewCVList.as_view(), name="viewcv_list"),
    path('home/', home,name="home"),
    path('indexx/', Indexx.as_view(),name="indexx"),
    path('findjob/<str:pk>/', JobListing.as_view(),name="findjob"),
    path('about/', About.as_view(),name="about"),
    path('contact/', Contact.as_view(),name="contact"),
    path('blog/', BlogList.as_view(),name="blog"),
    path("pdfgenerator/<int:pk>/", UserPDFView.as_view(), name="pdf-genertor"),
    path("termscondition/", TermsCondition.as_view(), name="termsandcondition"),
    path("jobdetail/<str:pk>/", Jobdetail.as_view(),name="jobdetail"),

]