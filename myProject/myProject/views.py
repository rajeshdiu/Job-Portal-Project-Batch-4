from django.shortcuts import render,redirect

from myApp.models import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



@login_required
def findjobPage(request):
    
    job=JobModel.objects.all()
    
    context={
        'job':job,
    }
    
    
    return render(request,"myAdmin/findjob.html",context)

@login_required
def jobdetailsPage(request,myid):
    
    job=JobModel.objects.get(id=myid)
    
    return render(request,"myAdmin/job_details.html",{'job':job})


@login_required
def blogPage(request):
    
    
    return render(request,"myAdmin/blog.html")


def logoutPage(request):
    
    logout(request)

    return redirect("registerPage")


def loginPage(request):
    
    if request.method=='POST':
        
        user_name=request.POST.get("username")
        password=request.POST.get("password")
        
        user=authenticate(username=user_name,password=password)
        
        if user:
            login(request,user)
            return redirect("dashboardPage")
    
    return render(request,"common/login.html")


def registerPage(request):
    
    if request.method=='POST':
        
        user_name=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        
        if password==confirm_password:
            
            user=User.objects.create_user(
                username=user_name,
                password=password,
            )
            user.email=email
            
            user.save()
            
            return redirect("loginPage")
            
    
    return render(request,"common/register.html")

@login_required
def dashboardPage(request):
    
    return render(request,"Dashboard/master.html")


@login_required
def addJobPage(request):
    
    if request.method=='POST':
        
        job_title=request.POST.get("job_title")
        company_name=request.POST.get("company_name")
        job_details=request.POST.get("job_details")
        job_type=request.POST.get("job_type")
        job_salary=request.POST.get("job_salary")
        job_location=request.POST.get("job_location")
        company_logo=request.FILES.get("company_logo")
        vacancy=request.POST.get("vacancy")
        application_deadline=request.POST.get("application_deadline")
        requirement=request.POST.get("requirement")
        education=request.POST.get("education")
        
        job=JobModel(
            job_title=job_title,
            company_name=company_name,
            job_details=job_details,
            job_type=job_type,
            job_salary=job_salary,
            job_location=job_location,
            company_logo=company_logo,
            vacancy=vacancy,
            application_deadline=application_deadline,
            requirement=requirement,
            education=education
            
        )
        
        job.save()
        
        return  redirect('viewJobList')

    
    return render(request,"Dashboard/addJob.html")


@login_required
def viewJobList(request):
    
    job=JobModel.objects.all()
    
    context={
        'job':job
    }
    
    return render(request,"Dashboard/viewJobList.html",context)


@login_required
def editJob(request,myid):
    
    job=JobModel.objects.get(id=myid)
    
    
    if request.method=='POST':
        
        job_id=request.POST.get("job_id")
        job_title=request.POST.get("job_title")
        company_name=request.POST.get("company_name")
        job_details=request.POST.get("job_details")
        job_type=request.POST.get("job_type")
        job_salary=request.POST.get("job_salary")
        job_location=request.POST.get("job_location")
        company_logo=request.FILES.get("company_logo")
        vacancy=request.POST.get("vacancy")
        application_deadline=request.POST.get("application_deadline")
        requirement=request.POST.get("requirement")
        education=request.POST.get("education")
        update_company_logo=request.POST.get("update_company_logo")
        
        job=JobModel(
            id=job_id,
            job_title=job_title,
            company_name=company_name,
            job_details=job_details,
            job_type=job_type,
            job_salary=job_salary,
            job_location=job_location,
            vacancy=vacancy,
            application_deadline=application_deadline,
            requirement=requirement,
            education=education
        )
        
        if company_logo:
            job.company_logo = company_logo
        
        
        job.save()
        
        return  redirect('viewJobList')


    context={
        'job':job
    }
    
    return render(request,"Dashboard/editJob.html",context)

@login_required
def deleteJob(req,myid):
    
    job=JobModel.objects.get(id=myid)
    
    job.delete()
    return  redirect('viewJobList')
