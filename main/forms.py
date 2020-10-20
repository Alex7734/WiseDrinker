from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper


class GetInfo(forms.Form):

    SEX_CHOICES = (
        ('M', 'Male',),
        ('F', 'Female',),
    )

    weight = forms.IntegerField(label='What is your weight? (kg/lb)')
    height = forms.IntegerField(label='What is your height? (cm/inches)')
    gender = forms.ChoiceField(choices = SEX_CHOICES)
    age = forms.IntegerField(label='What is your age?')
    time = forms.FloatField(label="How many hours since your first drink?")
    ate = forms.BooleanField(label="Check if you ate before drinking", required=False)


    def clean_kg(self):
        data = self.cleaned_data['kg']
        if 500 < data or data < 0:
            raise ValidationError("Kg must be between 1 and 500")
        return data

    def clean_age(self):
        data = self.cleaned_data['age']
        if 100 < data or data < 0:
            raise ValidationError("Age must be between 1 and 100")
        return data

    def clean_height(self):
        data = self.cleaned_data['height']
        if 250 < data or data < 0:
            raise ValidationError("Height must be between 1 and 250")
        return data

    def clean_time(self):
        data = self.cleaned_data['time']
        if data < 0:
            raise ValidationError("Time can not be negative!")
        return data

class RequestMeasurement(forms.Form):
    size = forms.IntegerField(label=None)

    def clean_data(self):
        data = self.clean_data['size']
        if data < 0:
            raise ValidationError("Can not drink a negative quantity!")
        return data

    def __init__(self, *args, **kwargs):
        super(RequestMeasurement, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'w-100'
            self.helper = FormHelper()
            self.helper.form_show_labels = False 



class ImperialOrMetric(forms.Form):

    MEASUREMENT = (
        ('ml', 'Metric (ml, kg, cm)',),
        ('oz', 'Imperial (oz, lb, in)',),
    )

    measurement = forms.ChoiceField(choices = MEASUREMENT)

class ResetTime(forms.Form):
    time = forms.FloatField(label="How many hours since your first drink?")
    check = forms.BooleanField(label="Do you want to also reset BAC and all entered drinks?", required=False)

    def clean_time(self):
        data = self.cleaned_data['time']
        if data < 0:
            raise ValidationError("Time can not be negative!")
        return data
