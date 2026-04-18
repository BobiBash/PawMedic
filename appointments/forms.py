from datetime import time

from django import forms
from django.forms.widgets import DateInput

from appointments.models import AppointmentSlot


def generate_timeslots():
    slots = []
    for hour in range(7, 21):
        for minute in (0, 30):
            t = time(hour, minute)
            label = t.strftime("%I:%M %p")
            value = t.strftime("%H:%M")
            slots.append((value, label))
    return slots

class VetScheduleForm(forms.Form):

    available_slots = forms.MultipleChoiceField(
        choices=generate_timeslots(),
        widget=forms.CheckboxSelectMultiple(attrs={
            "class": 'grid grid-cols-4 gap-x-4 gap-y-8 text-xl [&_label]:flex [&_label]:gap-1 w-fit [&_label]:w-fit',
        }),
        required=False,
    )

    selected_date = forms.DateField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = AppointmentSlot
        fields = ['date','time']

