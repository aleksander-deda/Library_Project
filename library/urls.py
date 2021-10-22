import debug_toolbar
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("users/", include("users.urls")),
    path("students/", include("students.urls")),
    path("books/", include("books.urls")),
]

if settings.DEBUG:
    urlpatterns.extend(
        [
            path("__debug__/", include(debug_toolbar.urls)),
        ]
    )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
