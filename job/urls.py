from django.urls import path  
from . import views 
from . import api

#.................
app_name = 'job'
urlpatterns = [
    path('',views.job_list,name ='job_list' ),
    path('add',views.add_job ,name= 'add_job'),
    path('<str:slug>',views.job_details ,name= 'job_detail'),
    ###apis
    path('api/list',api.joblistapi,name= 'joblistapi'),
    path('api/jobs/<int:id>',api.job_detail_api ,name= 'job_detail_api'),
    #class based View gen
    path('api/v2/jobs',api.JobListApi.as_view() ,name= 'JobListApi'),
    path('api/v2/jobs/<int:id>',api.JobDetail.as_view() ,name= 'JobDetail'),

]