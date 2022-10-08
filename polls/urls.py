from django.urls import path
from django.urls.conf import include
from . import views
from django.conf import settings
from . import views



ID = '<int:ID>'


urlpatterns = [
    path('<int:ID>', views.urlscreate, name='createindex'), #ES
    path('41_<int:ID>', views.urlscreateES, name='createindexitaly'), # ITALY
    path('21_<int:ID>', views.urlscreateSLOV , name='createindexslovakia'), # SLOVAKIA
    path('291_<int:ID>', views.urlscreateAUST, name='createindexaustia'), # AUSTRIA
    path('54_<int:ID>', views.urlscreateENGLD , name='urlscreateENGLD'), # ENGLAND 
    path('34_<int:ID>', views.urlscreatefrance , name='urlscreatefrance'), # Franche
]

