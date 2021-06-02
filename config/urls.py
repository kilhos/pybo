from django.contrib import admin
from django.urls import path, include
#from pybo import views
from pybo.views import base_views

urlpatterns = [
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('admin/', admin.site.urls),

    #path('', views.index, name='index'),    # / 페이지에 해당하는 urlpatterns
    path('', base_views.index, name='index'),
]
