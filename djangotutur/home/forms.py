from django import forms

from .models import Booking

class Bookingform(forms.modelform):
    class meta:
        model = Booking
        fields ='_all_'