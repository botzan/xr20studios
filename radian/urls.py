from django.conf.urls import *

import radian.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'radian.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



	url(r'^$', radian.views.home),

]
