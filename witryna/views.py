from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import PresentEvent
from .forms import PresentEventForm, ParticipantForm
from random import choice
from django.contrib.auth.decorators import login_required
def index(request):
	"""Strona główna dla witryny"""
	return render(request,"witryna/index.html")
@login_required
def wydarzenia(request):
	"""Strona z listą utworzonych wydarzeń"""
	events=PresentEvent.objects.order_by('?')
	context={"events":events}
	return render(request,"witryna/wydarzenia.html",context)
@login_required
def dod_wydarzenia(request):
	"""Dodaj nowe wydarzenie"""
	if request.method != 'POST':
		#Nie przekazano żadnych danych, należy utworzyć pusty formularz
		form=PresentEventForm()
	else:
		#Przekazano dane za pomocą żądania POST, nalezy je przetworzyć
		form=PresentEventForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('witryna:wydarzenia'))
	context={'form':form}
	return render(request,"witryna/dod_wydarzenia.html",context)
@login_required
def wydarzenie(request, event_id):
	"""Strona z wydarzeniem i listą uczestników"""
	event=PresentEvent.objects.get(id=event_id)
	participants=event.participant_set.all()
	context={"event":event, "participants":participants}
	return render(request,"witryna/wydarzenie.html",context)

@login_required
def dod_uczestnik(request, event_id):
	"""Dodaj nowego uczestnika"""
	event=PresentEvent.objects.get(id=event_id)
	if request.method != 'POST':
		#Nie przekazano żadnych danych, należy utworzyć pusty formularz
		form=ParticipantForm()
	else:
		#Przekazano dane za pomocą żądania POST, nalezy je przetworzyć
		form=ParticipantForm(request.POST)
		if form.is_valid():
			new_participant=form.save(commit=False)
			new_participant.present_event=event
			new_participant.owner=request.user
			new_participant.save()
			return HttpResponseRedirect(reverse('witryna:wydarzenie', args=[event_id]))
	context={'form':form, 'event':event}
	return render(request,"witryna/dod_uczestnik.html",context)
@login_required
def losowanie(request, event_id):
	event=PresentEvent.objects.get(id=event_id)
	participants=[]
	participants_all=event.participant_set.all()
	for participant in participants_all:
		participants.append(participant)
	participants_ordered=[]
	number=list(range(0,len(participants)))
	for pos in range(0,len(participants)):
		participants_ordered.append(participants[number.pop(choice(list(range(0,len(number)))))])
	for pos in range(0,len(participants_ordered)):
		if pos==0:
			participants_ordered[pos].taker=participants_ordered[pos+1].text
			participants_ordered[pos].giver=participants_ordered[-1].text
		elif pos==(len(participants_ordered)-1):
			participants_ordered[pos].taker=participants_ordered[0].text
			participants_ordered[pos].giver=participants_ordered[pos-1].text
		else:
			participants_ordered[pos].taker=participants_ordered[pos+1].text
			participants_ordered[pos].giver=participants_ordered[pos-1].text
		participants_ordered[pos].save()
	event.shuffled="yes"
	event.save()
	return HttpResponseRedirect(reverse('witryna:wydarzenie', args=[event_id]))
	
	
	

