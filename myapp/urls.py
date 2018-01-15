from django.conf.urls import url,include
from . import views

from django.contrib.auth import views as auth_views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^checklogin/$',views.check_login, name="check_login"),
    url(r'^search/$',views.search, name="search"),
    url(r'^employer-search/$',views.employer_search, name="employer_search"),
    url(r'^create-job/$',views.create_job, name="create_job"),
    url(r'^job/(?P<job_name>.*)/(?P<job_id>\d+)$',views.job_detail, name="job_detail"),
    url(r'^contactus/$',views.contact, name="contactus"),

    # url(r'^',  include('myapp.urls',namespace='mainapp')),
    # url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    # url(r'^logout/$', auth_views.logout,{'next_page': 'home'}, name='logout'),
    # url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    # url(r'^signup/$', views.signup, name='signup'),
    # url(r'^settings/$', views.profile, name="profile"),
    # url(r'^password/$', views.change_password, name='change_password'),

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
