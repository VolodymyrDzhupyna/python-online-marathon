from django.urls import path, include
from . import api_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', api_views.AuthorView)

urlpatterns=[
	path('', include(router.urls)),

]