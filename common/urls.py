from django.urls import path
from django.views.generic import TemplateView

from common.views import ReportIssue, ReportedIssuesList, ReportedIssuesDetail, ResolveIssueView

urlpatterns = [
    path('', TemplateView.as_view(template_name='common/home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='common/about.html'), name='about'),
    path('report-issue', ReportIssue.as_view(), name="report-issue"),
    path('issues-list', ReportedIssuesList.as_view(), name="reported-issues-list"),
    path('issue-detail/<int:pk>', ReportedIssuesDetail.as_view(), name="reported-issue-detail"),
    path('resolve-issue/<int:pk>', ResolveIssueView.as_view(), name='resolve-issue')
]