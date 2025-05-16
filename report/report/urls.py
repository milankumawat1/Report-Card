"""
URL configuration for report project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from reportcard.views import (
    login_page,
    logout_page,
    register_page,
    get_student,
    see_marks,
    send_email,
    delete_all_students,
    generate_fake_students,
    delete_all_users,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_student, name='home'),  # Added home page route
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register'),
    path('students/', get_student, name='get_students'),
    path('see_marks/<str:student_id>/', see_marks, name='see_marks'),
    path('send_email/', send_email, name='send_email'),
    path('delete_all_students/', delete_all_students, name='delete_all_students'),
    path('generate_fake_students/', generate_fake_students, name='generate_fake_students'),
    path('delete_all_users/', delete_all_users, name='delete_all_users'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
