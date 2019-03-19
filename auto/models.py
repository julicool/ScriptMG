from django.db import models

class userlogin(models.Model):
	username = models.CharField(max_length=50)
	passwd = models.CharField(max_length=100)
	authorizations = models.CharField(max_length=100)

class sys_dict(models.Model):
	dic_name = models.CharField(max_length=30)
	deploy_name = models.CharField(max_length=30)

class mobileinfo(models.Model):
	mobname = models.ForeignKey("sys_dict", on_delete=models.CASCADE)
	mobmodel = models.CharField(max_length=30)
	mobstat = models.IntegerField(default=1)
	resolution = models.CharField(max_length=30)
	system_type = models.CharField(max_length=10)
	system_numb = models.CharField(max_length=10)
	username = models.CharField(max_length=20, null=True)
	frist_time = models.IntegerField(null=True)
	last_time = models.IntegerField(null=True)
	create_time = models.IntegerField(default=1546272000)

