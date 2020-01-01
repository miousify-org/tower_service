from django.db import models
from django.db.models import CharField, TextField, IntegerField, DateTimeField, BooleanField

class Job(models.Model):
    miousify_domain_name=  CharField(max_length=20, editable=False, primary_key=True)
    created_at= DateTimeField(auto_created=True, editable=False)
    service_id= CharField(max_length=40, editable=False)
    plan= CharField(max_length=10, editable=False)
    is_trial= BooleanField()
    trial_started= DateTimeField(auto_created=True, editable=False)
    trial_ends= DateTimeField(auto_created=True, editable=False)
    is_running =  BooleanField()

class PlanConfiguration(models.Model):
    plan= CharField(max_length=10)
    instances = CharField(max_length=10)
    ram_limit= IntegerField()
    storage_capacity= IntegerField()

class Image(models.Model):
    version = CharField(max_length=20);
    full_name= CharField(max_length=30);
    comment= TextField()
    is_active= BooleanField()
# Create your models here.
