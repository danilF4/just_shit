from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('items.api.urls')),
    path('api-o-i/', include('items.api_o_i.urls')),
    path('api-orders/', include('items.api_orders.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-users/', include('users.api.urls')),
    #path('tokens/', include('rest_framework.authtoken.api.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
