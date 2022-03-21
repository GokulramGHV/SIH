from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *


class DateInput(forms.DateInput):
    input_type = "date"


class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "date_of_birth",
            "aadhaar_no",
        )
        widgets = {
            "date_of_birth": DateInput(),
        }


class TicketCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TicketCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Ticket
        fields = []
