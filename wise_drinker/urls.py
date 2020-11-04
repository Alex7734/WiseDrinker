from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_measurement, name="get_measurement"),
    path('get-info', views.get_info, name="get-info"),
    path('besafe', views.index, name="index"),
    path('add_drink/<int:pk>', views.add_drink, name="add-drink"),
    path('reset-bac', views.clear_bac, name="reset-bac"),
    path('redo-values', views.redo_values, name="redo-values"),
    path('reset-time-last-drink', views.rest_time_last_drink, name="reset-time-last-drink"),
    path('drink-info/<int:pk>', views.drink_info, name="drink-info"),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



