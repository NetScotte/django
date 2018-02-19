from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^user/list/',views.userlist,name='list'),
    url(r'^user/delete/',views.del_user,name='del'),
    url(r'^user/register/',views.register,name='edit'),
    url(r'^user/login/',views.require,name='require'),
    url(r'^user/logout/',views.Mylogout,name='logout'),
    url(r'',views.require,name='require')
]