from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='common/home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='common/about.html'), name='about')
]