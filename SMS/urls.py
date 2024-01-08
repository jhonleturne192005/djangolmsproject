from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500, handler400
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

urlpatterns = [
    # Estas URLs no serán prefijadas con el código del idioma
    path('admin/', admin.site.urls),
    path('accounts/api/', include('accounts.api.urls', namespace='accounts-api')),
    path('i18n/', include('django.conf.urls.i18n')),  # Incluye las URLs para el cambio de idioma
]

# URLs que serán prefijadas con el código del idioma
urlpatterns += i18n_patterns(
    path('', include('app.urls')),
    path('accounts/', include('accounts.urls')),
    path('programs/', include('course.urls')),
    path('result/', include('result.urls')),
    path('search/', include('search.urls')),
    path('quiz/', include('quiz.urls')),
    path('payments/', include('payments.urls')),
    prefix_default_language=False,  # Puede ser True si deseas que el idioma predeterminado tenga un prefijo también
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
