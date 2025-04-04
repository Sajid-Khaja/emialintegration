from django.contrib import admin
from django.urls import path
from mailer.views import (
    send_test_email,
    contact_view,
    dynamic_email_view,
    front_page
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', front_page, name='front_page'),  # 👈 Home page
    path('send-email/', send_test_email),
    path('contact/', contact_view, name='contact'),
    path('send-custom-email/', dynamic_email_view, name='send_custom_email'),
]
