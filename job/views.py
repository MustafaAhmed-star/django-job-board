from django.shortcuts import render,redirect
from .models  import Job
from django.core.paginator import Paginator
from django.urls import reverse
from .form import ApplyForm, JobForm
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

# Create your views here.
#............. 

def job_list(request):
    
 

    job_list = Job.objects.all()
    #search filter
    filter = JobFilter(request.GET, queryset=job_list )
    job_list =filter.qs
    #$
    paginator = Paginator(job_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'jobs': page_obj ,
        'count':job_list ,
        'filter':filter,
            }
    return render (request,'job/job_list.html',context  )
#............. 
def job_details(request , slug):
    job_details = Job.objects.get(slug=slug)
    if request.method =='POST':
        form =ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job =job_details 
            myform.save()
    else:
        form =ApplyForm()

    context ={'jobd':job_details,'form':form} 
    return render (request,'job/job_details.html',context)
#............. 
@login_required
def add_job(request):
    if request.method=='POST':
        form2=JobForm(request.POST,request.FILES)
        if form2.is_valid():
                myform=form2.save(commit=False)
                myform.owner=request.user
                myform.save()
                return redirect(reverse('job:job_list'))
    else:
        form2=JobForm()

    return render (request,'job/add_job.html',{'form2':form2})
