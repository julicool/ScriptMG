from django.db import models

class resultchart(models.Model):
	projectname = models.CharField(max_length=20)
	stime = models.CharField(max_length=20)
	etime = models.CharField(max_length=20)
	rtime = models.IntegerField()
	successrate = models.IntegerField()

class resultjs(models.Model):
	jsname = models.CharField(max_length=50)
	stime = models.CharField(max_length=20)
	errreason = models.CharField(max_length=3000)

class timejob(models.Model):
	stime = models.CharField(max_length=20)
	pjname = models.CharField(max_length=20)
	stat = models.IntegerField()