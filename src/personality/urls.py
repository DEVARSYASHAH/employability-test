
from django.urls import path
from django.views.generic import TemplateView

from personality import views

urlpatterns = [
    path('aptitude_test/', TemplateView.as_view(
        template_name='personality/aptitude_home.html'), 
        name='aptitude_home'),
    path('aptitude/test/', views.AptitudeTest.as_view(), name='aptitude_test'),
    path('aptitude/finished/', TemplateView.as_view(
        template_name='personality/aptitude_finished.html'),
        name='aptitude_finished'),
    path('test/', views.PersonalityTest.as_view(), name='personality_test'),
    path('completed/', views.PersonalityCompleted.as_view(), name='personality_completed'),
]
