from django.urls import path , include
from . import views 

app_name='accounts'

 
urlpatterns = [
    path('signup',views.SignUp,name ='SignUp' ),
    path('profile',views.profile,name ='profile' ),
    path('profile_edit',views.profile_edit,name ='profile_edit' ),
 
]