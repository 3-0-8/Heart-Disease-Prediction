from django.urls import path
from .import views


urlpatterns = [
    path('',views.Homepage,name='home' ),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('Input/',views.Input,name='Input'),
    path('prediction/',views.prediction,name='prediction'),
    path('report_user/',views.report_user,name='report_user'),
    path('graph_report/',views.report_graph,name='graph_report'),
   
    
]