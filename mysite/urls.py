"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from users import views as user_views
from counselors import views as counselors_views
from doctors import views as doctors_views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('register_specialist/', user_views.register_specialist,
         name='register_specialist'),
    # path('login/', authentication_views.LoginView.as_view(
    #    template_name='users\login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(
        template_name='users\home.html'), name='logout'),
    path('profile/', user_views.profilepage, name='profile'),
    path('counselors/', counselors_views.counselors, name='counselors'),
    path('testResult/', counselors_views.testResult, name='testResult'),
    path('doctors/', doctors_views.doctors, name='doctors'),
    path('doctors/testResult/', doctors_views.testResult, name='testResult'),
    path('test/', user_views.save_questions, name='test'),
    path('login/', user_views.loginPage, name='login'),
    path('testResult/assign', counselors_views.assign, name='assign'),
    path('doctors/testResult/assign', doctors_views.assign, name='assign'),
]


urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
