from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from api.router import router


urlpatterns = [
    path('api/', include((router.urls, 'api'))),
    path('admin/', admin.site.urls),
    path('custom_admin/', include(('custom_admin.urls', 'custom_admin'))),
    path('reviews/', include('reviews.urls')),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls')),
    path('support/', include('core.urls')),
    path('orders/', include('orders.urls')),
    path('', include('main.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'core.views.handler404'
handler403 = 'core.views.handler403'
