from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('galeria/',views.galeria,name='galeria'),
    path('lista_categorias/',views.lista_categorias,name='lista_categorias'),
    path('foto/<str:id>/',views.ver_foto,name='ver_foto'),
    path('agregar_foto',views.agregar_foto,name='agregar_foto'),


    path('registro_usuario/',views.registro_usuario,name='registro_usuario'),
    path('iniciar_sesion/',views.iniciar_sesion,name='iniciar_sesion'),
    path('perfil/',views.perfil_usuario,name='perfil'),
    path('cerrar_sesion/',views.cerrar_sesion,name='cerrar_sesion'),

    path('eliminar_usuario/<int:id>',views.eliminar_usuario,name='eliminar_usuario'),
    path('eliminar_foto/<int:id>',views.eliminar_foto,name='eliminar_foto'),
    path('eliminar_categoria/<int:id>',views.eliminar_categoria,name='eliminar_categoria'),
    path('actualizar_perfil/<int:id>',views.Actualizar_Perfil,name='Actualizar_Perfil'),
    # path('cambiar_contraseña/<int:id>',views.cambiar_contraseña,name='cambiar_contraseña'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

