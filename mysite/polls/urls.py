#imports from libraries
from django.urls import path

#import custome modules
from . import views

#namespacing
app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # /polls/
    path('<int:pk>/', views.DetailView.as_view(), name="detail"), # /polls/5/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"), # /polls/5/results/
    path("<int:question_id>/vote/", views.vote, name="vote"), # /polls/5/vote/
]