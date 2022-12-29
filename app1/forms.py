# form :-
# 1.djangoform> User Taable used>
# 2.manually models.py > table > manually validation> modelform.

from django.contrib.auth.models import User
from django.forms import ModelForm

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
