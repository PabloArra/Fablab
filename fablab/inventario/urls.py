from django.urls import path, include
from django.conf import settings
from inventario import views as inv_view
from django.contrib import admin
from usuarios import views as usuarios_view


urlpatterns = [
    path('',usuarios_view.login_user, name='login_user'), # pagina de inicio
    path('usuarios/registrar_user',usuarios_view.registrar_user, name='registrar_user'), # registrar usuario
    path('maquinas',inv_view.maquinas, name='maquinas'), # inventario de maquinas
    path('consumibles',inv_view.Consumibles, name='Consumibles'), # inventario de consumibles
    path('mantenimiento',inv_view.mantenimiento, name='Mantenimiento'), # En mantenimiento
    path('uso',inv_view.uso, name='En uso'), # En uso
    path('crearcate',inv_view.crearcate, name='crearcate'), # Crear categoria
    path('categoria',inv_view.crearmaq, name='crear'), # Crear maquina
    path('busqueda',inv_view.busquedamaq, name='busquedamaq'), # buscar maquinas
    path('editarm.html/<int:id>',inv_view.edit, name='edit'), # editar maquina
    path('borr/<int:n>',inv_view.borr, name='borr'), # borrar maquina
    path('consu',inv_view.crearconsu, name='crearconsu'), # crear consumible
    path('busquedaconsumible',inv_view.busquedaconsumible, name='busquedaconsumible'), # buscar consumible
    path('consuedit.html/<int:id>',inv_view.editconsu, name='editconsu'), # editar consumible
    path('borrcon/<int:n>',inv_view.borrconsu, name='borrconsu'), # borrar consumible
    path('solicitudes',inv_view.solic, name='solic'), # solicitud recibida
    path('solicitud',inv_view.enviar, name='enviar'), # solicitud enviada
    path('solicitudedit.html/<int:id>',inv_view.editarso, name='editarso'), # editar solicitud
    path('borrso/<int:n>',inv_view.borrarso, name='borrarso'), # borrar solicitud
    path('admuser',inv_view.Usuarios, name='admuser'), # registro de usuarios
    path('busquedausuario',inv_view.busquedausuario, name='busquedausuario'), # buscar usuario
    path('edituser.html/<int:id>',inv_view.edituser, name='edituser'), # editar usuario
    path('borrus/<int:n>',inv_view.borrus, name='borrus'), # borrar usuario
    path('logout/',usuarios_view.logout_user, name='logout_user'), # cerrar sesion
    path('admin/', admin.site.urls),


]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)