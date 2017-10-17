from django.conf.urls import *

import xr20studios.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'xr20studios.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



	url(r'^$', xr20studios.views.home),

]
