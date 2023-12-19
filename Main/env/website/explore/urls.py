from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPage, name="LandingPage"),
    path('AfterRegistration/', views.AfterRegistration, name="AfterRegistration"),
    path('explore/', views.explore, name="explore"),
    path('quiz/', views.quiz, name="quiz"),
    path('result/', views.result, name="result"),
    path('c1/', views.c1, name="c1"),
    path('c2/', views.c2, name="c2"),
    path('c3/', views.c3, name="c3"),
    path('c4/', views.c4, name="c4"),
    path('c5/', views.c5, name="c5"),
    path('c6/', views.c6, name="c6"),
    path('c7/', views.c7, name="c7"),
    path('c8/', views.c8, name="c8"),
    path('c9/', views.c9, name="c9"),
    path('c10/', views.c10, name="c10"),
    path('c11/', views.c11, name="c11"),
    path('c12/', views.c12, name="c12"),
    path('c13/', views.c13, name="c13"),
    path('c14/', views.c14, name="c14"),
    path('c15/', views.c15, name="c15"),
    path('c16/', views.c16, name="c16"),
    path('c17/', views.c17, name="c17"),
    path('c18/', views.c18, name="c18"),]