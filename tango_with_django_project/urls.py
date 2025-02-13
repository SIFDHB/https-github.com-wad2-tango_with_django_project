"""tango_with_django_project URL Configuration

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
from django.contrib import admin
from django.urls import include, path
from . import views 

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
	
    # e.g. /polls/
    path('', views.index, name='index'),
    # e.g. /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # e.g. /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # e.g. /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'), 
]