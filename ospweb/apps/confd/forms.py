from django import forms
from confd.models import project_Confd, vhosts_Confd


class ProjectForm(forms.ModelForm):
    class Meta:
        model = project_Confd
        fields = "__all__"


class VhostForm(forms.ModelForm):
    class Meta:
        model = vhosts_Confd
        fields = ['project_name','vhosts_key','vhosts_value']