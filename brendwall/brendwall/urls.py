from django.contrib import admin
from django.urls import path, include
from productAPI.views import main_page
urlpatterns = [
	path('', main_page, name='main_page'),
	path('admin/', admin.site.urls),
	path('api/', include('productAPI.urls'))
]
