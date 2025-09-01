from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/beneficiaries/', include('beneficiaries.urls')),
    path('api/policies/', include('policies.urls')),
    path('api/claims/', include('claims.urls')),
]