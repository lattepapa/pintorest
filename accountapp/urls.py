from django.urls import path

from accountapp.views import hell_world, AccountCreateView

app_name = 'accountapp'
urlpatterns=[
    path('hell_world/', hell_world, name='hell_world'),
    path('create/', AccountCreateView.as_view(), name='create'),
]