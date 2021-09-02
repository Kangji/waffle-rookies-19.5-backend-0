from django.urls import include, path

from survey import views

urlpatterns = [
    path('results/', views.get_survey_results, name="get_surveys"),
    path('results/<survey_id>/', views.get_survey, name="get_survey"),
    path('os/', views.get_os_all, name="get_os_all"),
    path('os/<os_id>/', views.get_os, name="get_os"),
]
