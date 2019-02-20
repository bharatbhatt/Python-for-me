from django.urls import path
from testapp2 import views
urlpatterns = [
    path('info1/',views.info_view1),
    path('info2/',views.info_view2),
]
