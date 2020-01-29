from .models import Game
from django import forms
from django.contrib.auth import get_user_model


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('defender', 'att_choice',)
        labels = {
            'defender': '상대방',
            'att_choice': '무기 선택'
        }
    def __init__(self, username, *args, **kwargs) -> object:
        super(ChallengeForm, self).__init__(*args, **kwargs)
        self.fields['defender'].queryset = get_user_model().objects.all().exclude(username=username)
        #https://simpleisbetterthancomplex.com/questions/2017/03/22/how-to-dynamically-filter-modelchoices-queryset-in-a-modelform.html


class AcceptChallengeForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('dfd_choice',)
        labels = {
            'dfd_choice': '방어 무기 선택'
        }