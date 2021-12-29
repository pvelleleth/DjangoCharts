from django.contrib import admin
from .models import ArticleData, ClinicalData, JointData
# Register your models here.

admin.site.register(ArticleData)
admin.site.register(ClinicalData)
admin.site.register(JointData)
