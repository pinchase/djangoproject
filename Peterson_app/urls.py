from django.urls import path
from Peterson_app import views
urlpatterns=[
path('',views.home,name='My_index'),
    path('about/',views.about,name='My_about'),
    path('contact/',views.contact,name='My_contact'),
    path('blog/',views.blog,name='My_blog'),
    path('services/',views.services,name='My_services'),
    path('assignment/',views.assignment,name='My_assignment'),


]