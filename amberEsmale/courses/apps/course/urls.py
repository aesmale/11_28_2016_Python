from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add_course),
    url(r'^add_user$', views.add_user),
    url(r'^remove/(?P<id>\d+)$', views.remove_course),
    url(r'^users_course$', views.add_users_courses),
    url(r'^enroll$', views.enroll)
]
