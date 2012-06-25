from django.db import models
from django import forms
from django.forms import ModelForm

class EmailRequest(models.Model):
    email = models.EmailField("email address")
    dateCreated = models.DateTimeField("date created", auto_now_add=True)


class EmailRequestForm(ModelForm):

    class Meta:
        model = EmailRequest
        fields = ('email',)