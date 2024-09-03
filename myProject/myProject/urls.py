from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', findjobPage,name="findjobPage"),
    path('loginPage/', loginPage,name="loginPage"),
    path('registerPage/', registerPage,name="registerPage"),
    path('jobdetailsPage/<str:myid>', jobdetailsPage,name="jobdetailsPage"),
    path('blogPage/', blogPage,name="blogPage"),
    path('dashboardPage/', dashboardPage,name="dashboardPage"),
    path('addJobPage/', addJobPage,name="addJobPage"),
    path('viewJobList/', viewJobList,name="viewJobList"),
    path('editJob/<str:myid>', editJob,name="editJob"),
    path('deleteJob/<str:myid>', deleteJob,name="deleteJob"),
    path('logoutPage/', logoutPage,name="logoutPage"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
