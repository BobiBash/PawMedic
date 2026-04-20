import json
from datetime import datetime, timedelta
from time import strftime, strptime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.views import View


from django.views.generic import CreateView, TemplateView, ListView
from pygments.lexer import default

from appointments.forms import VetScheduleForm
from appointments.models import Appointment, AppointmentSlot
from pets.models import Pet


# Create your views here.
class VetScheduleView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = "appointments.change_appointmentslot"

    def get(self, request, slug):

        form = VetScheduleForm()

        registered_timeslots = AppointmentSlot.objects.filter(vet_id=request.user.vet_profile.id).values(
            'date', 'time'
        )

        return render(request, "appointments/manage_schedule.html", context={
            "form": form,
            "slots": json.dumps(list(registered_timeslots), default=str)
        })

    def post(self, request, slug):

        form = VetScheduleForm(request.POST)


        if form.is_valid():
            vet_id = request.user.vet_profile.id
            AppointmentSlot.objects.filter(vet_id=vet_id).delete()
            date = form.cleaned_data['selected_date']
            times = form.cleaned_data['available_slots']
            for time in times:
                formatted_time = datetime.strptime(time, '%H:%M').time()
                formatted_datetime = datetime.combine(date, formatted_time)
                AppointmentSlot.objects.create(date=date, time=formatted_time, vet_id=vet_id, date_and_time=formatted_datetime)
            return redirect('vet-schedule', slug=slug)

        messages.error(request, "No timeslots selected. Please select at least one available timeslot to continue.")
        return redirect('vet-schedule', slug=slug)



class UserMakeAppointMentView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = "appointments.add_appointment"

    def post(self, request, slug):
        owner_id = request.user.pk
        slot_id = request.POST.get("slot")
        pet_id = request.POST.get("pet")
        pet = get_object_or_404(Pet, pk=pet_id)
        if not pet.owner == request.user:
            return redirect("home")

        Appointment.objects.create(vet_id=owner_id, slot_id=slot_id, pet_id=pet_id)

        return redirect("vets-list")


class UserAppointmentsView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "appointments.view_appointment"
    model = Appointment
    template_name = "accounts/user_appointments.html"
    context_object_name = "appointments"

    def get_queryset(self):
        return Appointment.objects.filter(vet=self.request.user)
