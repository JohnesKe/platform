from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from core import views as core_views
from authentication import views as mentor_auth_views
from activities import views as activities_views
from search import views as search_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    url(r'^mentors/$', core_views.mentors, name='mentors'),
    url(r'^mentees/$', core_views.mentees, name='mentees'),
    url(r'^setup/$', core_views.initial_setup, name='initial_setup'),
    # User URLs
    url(
        r'^account/login',
        auth_views.login, {'template_name': 'core/cover.html'},
        name='login'),
    url(
        r'^account/logout',
        auth_views.logout, {'next_page': '/'},
        name='logout'),
    url(r'^account/signup/$', mentor_auth_views.signup, name='signup'),
    url(r'^account/forgot_pass/$', auth_views.password_reset, {
        'template_name': 'authentication/password_reset.html',
        'email_template_name': 'authentication/password_reset_email.html'
    }, "forgot_password"),
    url(
        r'^account/forgot_pass_confirm/(?P<uidb64>[^/]+)/(?P<token>[^/]+)/$',
        auth_views.password_reset_confirm, {
            'template_name': 'authentication/password_reset_confirm.html',
            'post_reset_redirect': '/account/forgot_pass_complete/'
        },
        name='password_reset_confirm'),
    url(
        r'^account/forgot_pass_done/',
        auth_views.password_reset_done,
        {'template_name': 'authentication/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^account/forgot_pass_complete/', auth_views.password_reset_complete,
        {'template_name': 'authentication/password_reset_complete.html'}),
    url(
        r'^account/forgot_pass_confirm/(?P<uidb64>[^/]+)/(?P<token>[^/]+)/$',
        auth_views.password_reset_confirm,
        {'template_name': 'authentication/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^questions/', include('questions.urls'), name='questions'),
    url(r'^messages/', include('messenger.urls')),
    url(
        r'^notifications/$',
        activities_views.notifications,
        name='notifications'),
    url(
        r'^notifications/last/$',
        activities_views.last_notifications,
        name='last_notifications'),
    url(
        r'^notifications/check/$',
        activities_views.check_notifications,
        name='check_notifications'),
    url(r'^search/$', search_views.search, name='search'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
    url(r'^u/(?P<username>[\w@.-]+)/$', core_views.profile, name='profile'),
]

urlpatterns += [
    url(r'^interests/', include('interests.urls')),
]

urlpatterns += [
    url(r'^milestones/', include('milestones.urls')),
]


admin.site.site_title = 'Mentor001 Adminstration'
admin.site.site_header = 'Mentor001 Adminstration'
