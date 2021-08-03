from django import forms
from .models import PresentEvent, Participant
class PresentEventForm(forms.ModelForm):
	class Meta:
		model=PresentEvent
		fields=["text"]
		labels={"text":"Podaj nazwę wydarzenia"}
class ParticipantForm(forms.ModelForm):
	class Meta:
		model=Participant
		fields=["text"]
		labels={"text":"Podaj swoje imię"}
