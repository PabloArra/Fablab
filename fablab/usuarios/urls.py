from django.urls import path
from usuarios import views as usuarios_view


urlpatterns = [
    path('login_user',usuarios_view.login_user, name='login_user'),
    path('registrar_user',usuarios_view.registrar_user, name='registrar_user'),
    path('logout/',usuarios_view.logout_user, name='logout_user'),

]
