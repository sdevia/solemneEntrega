from django.conf.urls import url

from .views import index_Adopcion

urlpatterns = [
    url(r'^$', index_Adopcion),

]