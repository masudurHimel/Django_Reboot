from django import forms
from first_app.models import Topic

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget= forms.Textarea)


class TopicInfoUpdater(forms.ModelForm):
    class Meta():
        model = Topic
        fields = "__all__"
