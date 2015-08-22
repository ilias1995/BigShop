from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', 'apps.views.index', name='index'),
    url(r'^cars/', 'apps.views.cars', name='cars'),
    url(r'^cars_info/(?P<id>\d+)/', 'apps.views.info_car', name='info_car'),
    url(r'^form_car/(?P<type_for_car_id>\d+)/$', 'apps.views.spare_parts', name='spare_parts'),
    url(r'^info_space_parts/(?P<id>\d+)/', 'apps.views.info_spare_parts', name='info_spare_parts'),
    # Examples:
    # url(r'^$', 'bigshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

