from django.conf.urls import url,include
from website import views
urlpatterns = [
    url(r'^id3$',views.id3_page),
]