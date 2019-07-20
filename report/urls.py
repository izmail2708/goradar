from django.urls import path
from . import views
from .decorators import check_recaptcha

urlpatterns = [
    path('', views.report, name='report'),
    path('greenzone/', check_recaptcha(views.report_greenzone), name='report_greenzone'),
    path('roadnetwork/', check_recaptcha(views.report_roadnetwork), name='report_roadnetwork'),
    path('transition/', check_recaptcha(views.report_transition), name='report_transition'),
    path('stoppingpoint/', check_recaptcha(views.stopping_point), name='stopping_point'),
    path('waterbody/', check_recaptcha(views.report_waterbody), name='report_waterbody'),
    path('yard/', check_recaptcha(views.report_yard), name='report_yard'),
    path('buildings/', check_recaptcha(views.report_buildings), name='report_buildings'),
]
