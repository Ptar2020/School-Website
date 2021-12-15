from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firstApp.urls')),
    path('administration/', include('secondApp.urls')),
    path('theschool/', include('about_the_school.urls')),
    path('developer/', include('about_developer.urls')),
    path('departments/', include('departments.urls')),
    path('downloads/', include('files.urls')),
    path('accounts/', include('accounts.urls')),
    path('background/', include('background_photos.urls')),
    path('events/',include('eventuals.urls')),
    path('scroll/',include('scrolltext.urls')),

]
urlpatterns = urlpatterns +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
