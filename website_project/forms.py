from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Add any additional logic here
        if commit:
            instance.save()
        return instance
class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField(max_length=80)
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)
