from django.contrib import admin
from django.urls import path, include

import tracker.urls
import ajax_select.urls

urlpatterns = [
    path('admin/lookups/', include(ajax_select.urls)),
    path('admin/', admin.site.urls),
    path('tracker/', include(tracker.urls, namespace='tracker')),
]