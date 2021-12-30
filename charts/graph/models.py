from django.db import models

# Create your models here.

class ArticleData(models.Model):
    yearRange = models.CharField(max_length=220)
    count = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.yearRange, self.count)

class ClinicalData(models.Model):
    country = models.CharField(max_length=220)
    num = models.FloatField()

    def __str__(self):
        return "{}-{}".format(self.country, self.num)

class JointData(models.Model):
    disease = models.CharField(max_length=220)
    refs = models.IntegerField()
    trials = models.IntegerField()

    def __str__(self):
        return "{}-{}-{}".format(self.disease, self.refs, self.trials)