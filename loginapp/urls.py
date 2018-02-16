from django.conf.urls import url,include
from . import views

from django.contrib.auth import views as auth_views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # url(r'^$', views.home, name='home'),
    # url(r'^',  include('myapp.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page': 'home'}, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^signup-1/$', views.choose_signup, name='choose_signup'),
    url(r'^signup-2/$', views.job_signup, name='job_signup'),
    url(r'^signup-2-2/(?P<uid>\d+)$', views.job_signup2, name='job_signup2'),
    url(r'^signup-company/$', views.company_signup, name='company_signup'),
    url(r'^signup-company-2/(?P<uid>\d+)$', views.company_signup2, name='company_signup2'),
    url(r'^signup-success/$', views.signup_success, name='signup_success'),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^company-profile/$', views.company_profile, name="company_profile"),
    url(r'^disable-settings/$', views.edit_disable_profile, name="edit_disable_profile"),
    url(r'^company-settings/$', views.edit_company_profile, name="edit_company_profile"),
    url(r'^password/$', views.change_password, name='change_password'),
    

    url(r'^settings/notifications$', views.profile_noti, name="profile_noti"),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)