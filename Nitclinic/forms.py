from django  import forms
from Nitclinic.models import patient,user_login


class patientform(forms.ModelForm):
    class Meta:
        model=patient
        fields="__all__"
class userform(forms.ModelForm):
    class Meta:
        model= user_login
        fields="__all__"