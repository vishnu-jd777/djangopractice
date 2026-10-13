from django.forms import ModelForm
from . models import bmwlist

class bmwform(ModelForm):
    class Meta:
        model=bmwlist
        fields='__all__'