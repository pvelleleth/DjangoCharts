
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ArticleData, ClinicalData, JointData

# Create your views here.

class article_view(TemplateView):
    template_name = 'graph/article_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = ArticleData.objects.all()
        return context

class clinical_view(TemplateView):
    template_name = 'graph/clinical_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = ClinicalData.objects.all()
        return context

class joint_view(TemplateView):
    template_name = 'graph/joint_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = JointData.objects.all()
        return context

class home(TemplateView):
    template_name = 'graph/home.html'