from django.db import models

class Campaign(models.Model):
	title = models.CharField(max_length=200)
	desc = models.TextField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()

class Politician(models.Model):
	name = models.CharField(max_length=200)
	party = models.ForeignKey(Party)
	desc = models.TextField()

class Party(models.Model):
	name = models.CharField(max_length=200)

class PoliticianCampaign(models.Model):
	campaign = models.ForeignKey(Campaign)
	politician = models.ForeignKey(Politician)
	desc = models.TextField()

class Contact(models.Model):
	type = modes.CharField(max_length=25)
	politician = models.ForeignKey(Politician)
	address = models.CharField(max_length=200)

class Action(models.Model):
	campaign = models.ForeignKey(Campaign)
	contact = models.ForeignKey(Contact)
	text = models.TextField()
	date = models.DateTimeField(auto_now=True)
	ip = models.IPAddressField()

class Response(models.Model):
	campaign = models.ForeignKey(Campaign)
        contact = models.ForeignKey(Contact)
        text = models.TextField()
	date = models.DateTimeField(auto_now=True)
        ip = models.IPAddressField()
	
