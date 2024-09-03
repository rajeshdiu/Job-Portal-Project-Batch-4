from django.db import models


class JobModel(models.Model):
    
    JOB_TYPE=[
        ('full_time','Full Time'),
        ('part_time','Part Time'),
    ]
    
    job_title=models.CharField(max_length=100,null=True)
    company_name=models.CharField(max_length=100,null=True)
    job_details=models.TextField(max_length=100,null=True)
    job_type=models.CharField(choices=JOB_TYPE, max_length=100,null=True)
    job_salary=models.CharField(max_length=100,null=True)
    job_location=models.CharField(max_length=100,null=True)
    company_logo=models.ImageField(upload_to='Media/Company_logo',null=True)
    vacancy=models.PositiveIntegerField(null=True)
    application_deadline=models.DateField(null=True)
    requirement=models.TextField(null=True)
    education=models.TextField(null=True)
    
    
    create_at=models.DateField(auto_now_add=True,null=True)
    
    
    
