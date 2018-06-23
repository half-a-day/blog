from django.conf.urls import url
from main import views as main_views

app_name = 'main'
urlpatterns = [
	url(r'^$',main_views.IndexView.as_view(),name='index'),
	url(r'^post/(?P<pk>[0-9]+)/$',main_views.PostDetailView.as_view(),name='detail'),
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',main_views.ArchivesView.as_view(),name='archives'),
	url(r'^category/(?P<pk>[0-9]+)/$',main_views.CategoryView.as_view(),name='category'),
	
	]