from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views
from registration.forms import RegistrationFormUniqueEmail


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('game.urls')),
    url(r'^profile/', include('user_profile.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, {'next_page': '/'}, name='logout'),

    # url(r'^register/$', RegistrationFormUniqueEmail.as_view(), name='registration_register'),
    # url(r'^register/$', 'registration.views.register', {'form': RegistrationFormUniqueEmail}, name='registration_register'),

    # url('', include('registration.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^accounts/', include('registration.urls')),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
