import datetime


def delete_unpaiduser(self):
    current_date = datetime.datetime.now()
    a= User.objects.filter(paymentend_date=current_date)
    print(a)
    if a:
        a.delete()
        a.save()
        print('done')



USERTYPE_CHOICES =(
    ("Job Seeker", "Job_seeker"),
    ("Company", "Company"),
    ("Admin", "Admin"),

)
CV_CHOICES =(
    ("Accepted", "accepted"),
    ("Rejected", "rejected"),
    ("Not Viewed", "notview"),

)


JOB_CHOICES =(
    ("Part Time", "parttime"),
    ("Full Time", "fulltime"),
    ("Freelancing", "freelance"),
    ("Remote", "remote"),

)


Job_seeker = 'Job_seeker'
Company = 'Company'
Admin = "Admin"

PAYMENT_CHOICES =(
    ("Bank Transfer", "banktransfer"),
    ("Esewa", "esewa"),
    ("Khalti", "khalti"),
    ("PayPal", "paypal"),
    ("Connect ips", "Connectips"),
)

PAY_CHOICES=(
    ("Paid", "paid"),
    ("Un Paid", "unpaid"),
    ("Partial Payment", "patial"),
)
CATEGORY_CHOICES=(
    ("Digital Work", "digital"),
    ("Field Work", "field"),
    ("Freelancing Work", "freelancing"),

)



EDUCATION_CHOICES=(
    ("Bachelor", "bachelor"),
    ("Master", "master"),
    ("Other", "other"),
)

POSITION_CHOICES=(
    ("Senior", "senior"),
    ("Junior", "Junior"),
    ("Intern", "intern"),
    ("Mid-Level", "midlevel"),

)

SKILL_CHOICES=(
    ("Technical Skills", "technical"),
    ("Soft Skills", "soft"),
)