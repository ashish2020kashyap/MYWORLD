
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title="Myworld API",
        default_version='v1',
        #description="Test description",
        #terms_of_service="https://www.ourapp.com/policies/terms/",
        #contact=openapi.Contact(email="contact@expenses.local"),
        #license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('social_auth/', include(('social_auth.urls', 'social_auth'),
                                 namespace="social_auth")),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),

    path('api/api.json/', schema_view.without_ui(cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),

    re_path(r'query/?', include('GraphQl.urls')),
    re_path(r'follow/?', include('Followers.urls')),
    re_path(r'profile/?', include('Profile.urls')),
    re_path(r'comment/?', include('Comment.urls')),
    re_path(r'like/?', include('Like.urls')),
    re_path(r'video/?', include('Videos.urls')),
    re_path(r'searchengine/?', include('SearchEngine.urls')),
    url(r'^image/', include('Discovery.urls')),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
