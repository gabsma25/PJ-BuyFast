from django.contrib import admin
from django.urls import path
from .views import home_page, about_page, contact_page, login_page, register_page

from django.conf import settings
from django.conf.urls.static import static

from products.views import ProductListView,ProductDetailView

urlpatterns = [
        path('', home_page),
        path('about/', about_page),
        path('contact/', contact_page),
        path('admin/', admin.site.urls),
        path('login/', login_page),
        path('register/', register_page),
        path('products/', ProductListView.as_view()),
        path('products/<int:pk>', ProductDetailView.as_view()),
        path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
