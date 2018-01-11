from django.conf.urls import url,include
from . import views

from django.contrib.auth import views as auth_views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # url(r'^$', views.home, name='home'),
    url(r'^',  include('myapp.urls',namespace='mainapp')),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page': 'home'}, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^signup-1/$', views.choose_signup, name='choose_signup'),
    url(r'^signup-2/$', views.job_signup, name='job_signup'),
    url(r'^signup-2-2/$', views.job_signup2, name='job_signup2'),
    # return redirect('job_signup2')
    url(r'^signup-company/$', views.company_signup, name='company_signup'),
    url(r'^signup-company-2/$', views.company_signup2, name='company_signup2'),
    url(r'^signup-success/$', views.signup_success, name='signup_success'),
    url(r'^settings/$', views.profile, name="profile"),
    # url(r'^password/$', views.change_password, name='change_password'),

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
