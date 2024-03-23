from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    VILLAGE_CHOICES = [
        'Gandhinagar',
        'Valiwade',
        'Chinchwad',
    ]

    village = forms.ChoiceField(choices=[(village, village) for village in VILLAGE_CHOICES], required=True)

    class Meta:
        model = UserProfile
        fields = ['name', 'village', 'phone_number', 'photo']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['photo'].required = False
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['village'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control-file', 'accept': 'image/*'})
