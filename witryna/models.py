from django.db import models
from django.contrib.auth.models import User
class PresentEvent(models.Model):
	text=models.CharField(max_length=20)
	def __str__(self):
		return self.text
	shuffled=models.CharField(max_length=20,default="no")
class Participant(models.Model):
	present_event=models.ForeignKey(PresentEvent,
	on_delete=models.CASCADE)
	text=models.TextField()
	owner=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	class Meta:
		verbose_name_plural="participants"
	def __str__(self):
		return self.text
	taker=models.CharField(max_length=20,default="nie podano")
	giver=models.CharField(max_length=20,default="nie podano")
