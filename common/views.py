from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView

from PawMedic import settings
from common.forms import ReportIssueForm
from common.models import ReportedIssues


# Create your views here.
class ReportIssue(LoginRequiredMixin, CreateView):
    template_name = 'common/report_issue.html'
    form_class = ReportIssueForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class ReportedIssuesList(LoginRequiredMixin, ListView):
    template_name = "common/reported_issues_list.html"
    context_object_name = 'issues_list'
    queryset = ReportedIssues.objects.all()

class ReportedIssuesDetail(LoginRequiredMixin, DetailView):
    template_name = "common/reported_issue_detail.html"
    context_object_name = "issue"

    def get_queryset(self):
        return ReportedIssues.objects.filter(pk=self.kwargs['pk'])

class ResolveIssueView(LoginRequiredMixin, View):

    def get(self, request, pk):
        title = ReportedIssues.objects.filter(pk=pk).values_list('title', flat=True).first()
        context = {
            'title': title,
            'pk': pk,
        }
        return render(request, 'common/resolve_issue.html', context)

    def post(self, request, pk):
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email]
        )

        ReportedIssues.objects.filter(pk=pk).delete()

        return redirect('reported-issues-list')
