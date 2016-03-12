from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('game.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, {'next_page': '/'}, name='logout'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
