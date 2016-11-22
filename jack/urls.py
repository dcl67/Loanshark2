from django.conf.urls import url, include

from .views import AddJack, DeleteJack, EditJackInfo, index, ExportCSV, SwapView

urlpatterns = (
    # url(r'^$', landing_page, name='') home page?
    url(r'^$', index, name='jack'),
    url(r'^add/', AddJack, name='addjack'),
    url(r'^update/(?P<pk>[0-9]+)/$', EditJackInfo, name='editjack'),
    url(r'^search/', include('haystack.urls')),
    url(r'^delete/(?P<id>[0-9]+)/$', DeleteJack, name='deletejack'),
    url(r'^export/', ExportCSV, name='export'),
    url(r'^swap/', SwapView, name='swap'),
)