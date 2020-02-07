from django.conf.urls import url

from instagram.views import *

urlpatterns = [
    url (r'^$', view_mainPage),
    url (r'^detail/(?P<id>[0-9]+)/$', view_board_detail),
    url (r'^login/$', view_login_page),
    url (r'^user/$', Dologin),
    
    url (r'^board/$', post_board_contents),
    url (r'^comment/$', post_comment_contents),

    url (r'^like/board/(?P<id>[0-9]+)/$', like_board),
    url (r'^like/comment/(?P<id>[0-9]+)/$', like_comment),

]   
