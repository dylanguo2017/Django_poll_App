from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
	# we define a question_text field, it is modeled by models module CharFiled method
	# max_length is a keyword argument of CharField method
	question_text=models.CharField(max_length=200)
	# second field of our Question Model is pub_date
	# the positional argument for DateTimeField probably is name, here we assign
	#"date published" to it
	pub_date= models.DateTimeField('date published') 
	def __str__ (self):
		return self.question_text


	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	#foreign key will be an entry also show up in another table which is unique
	question=models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	def __str__ (self):
		return self.choice_text

