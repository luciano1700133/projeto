"""lmsimpacta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import index, contato, curso, ads, adm, enfermagem, fisioterapia, footer, header, institucional, new1, noticias, detalhe_adm, detalhe_ads, detalhe_enf

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^contato', contato),
    url(r'^curso', curso),
    url(r'^ads', ads),
    url(r'^adm', adm),
    url(r'^enfermagem', enfermagem),
    url(r'^footer', footer),
    url(r'^header', header),
    url(r'^institucional', institucional),
    url(r'^new1', new1),
    url(r'^noticias', noticias),
    url(r'^fisioterapia', fisioterapia),
    url(r'^detalhe_adm', detalhe_adm),
    url(r'^detalhe_ads', detalhe_ads),
    url(r'^detalhe_enf', detalhe_enf)
]
