from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^search/$',views.search, name="search"),
    url(r'^employer-search/$',views.employer_search, name="employer_search"),
    url(r'^job/(?P<job_name>.*)/(?P<job_id>\d+)$',views.job_detail, name="job_detail"),
    url(r'^detail/(?P<job_name>.*)/(?P<job_id>\d+)/(?P<noti_id>\d+)$',views.click_noti, name="click_noti"),
    url(r'^profile/(?P<dis_id>\d+)/(?P<job_id>\d+)$',views.disable_detail, name="dis_detail"),
    url(r'^request-job/(?P<dis_id>\d+)/(?P<job_id>\d+)$',views.invite_job_to_disability, name="request_job"),
    url(r'^contactus/$',views.contact, name="contactus"),
    url(r'^search-job/$', views.disable_search_job, name='disable_search_job'),
    url(r'^search-disability-person/$', views.employer_search_disability, name='employer_search_disability'),
    url(r'^notifications/$',views.notification_mobile, name="noti"),
    url(r'^confirm/(?P<job_name>.*)/(?P<job_id>\d+)$',views.confirm_job, name="confirm_job"),
    url(r'^confirm_job/(?P<dis_id>\d+)/(?P<job_id>\d+)$',views.confirm_job, name="confirm_job"),
    url(r'^apply_job/(?P<dis_id>\d+)/(?P<job_id>\d+)$',views.apply_job, name="apply_job")
    url(r'^notificationsall/$',views.show_notifications, name="show_notifications")
  
    

    # url(r'^contactus/$',views.contact, name="contactus"),


    # url(r'^',  include('myapp.urls',namespace='mainapp')),
    # url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    # url(r'^logout/$', auth_views.logout,{'next_page': 'home'}, name='logout'),
    # url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    # url(r'^signup/$', views.signup, name='signup'),
    # url(r'^settings/$', views.profile, name="profile"),
    # url(r'^password/$', views.change_password, name='change_password'),

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
