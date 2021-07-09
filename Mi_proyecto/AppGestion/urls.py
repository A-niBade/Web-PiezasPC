from django.urls import path
from .views import home, procesadores, placas_madre, tarjeta_video, ingresar,ingresar_placa, ingresar_procesador, ingresar_tarjeta, busqueda, lista_placas, lista_procesadores, lista_tarjetas, modificar_proce, modificar_placa,modificar_tarjeta, eliminar_placa, eliminar_proce, eliminar_tarjeta

urlpatterns = [
    path('', home, name= "home"),
    path('procesadores/', procesadores, name= "procesadores"),
    path('tarjetas-video/', tarjeta_video, name= "tarjetas_video"),
    path('placas-madre/', placas_madre, name= "placas_madre"),
    path('ingresar/', ingresar, name = "ingresar"),
    path('ingresar/ingresar-placa', ingresar_placa, name = "ingresar_placa"),
    path('ingresar/ingresar-tarjeta', ingresar_tarjeta, name = "ingresar_tarjeta"),
    path('ingresar/ingresar-procesador', ingresar_procesador, name = "ingresar_procesador"),
    path('busqueda/', busqueda, name = "busqueda"),
    path('busqueda/lista-placas/', lista_placas, name = "lista_placas"),
    path('busqueda/lista-procesadores/', lista_procesadores, name = "lista_procesadores"),
    path('busqueda/lista-tarjetas/', lista_tarjetas, name = "lista_tarjetas"),
    path('modificar_proce/<id>/', modificar_proce, name = "modificar_proce"),
    path('modificar_placa/<id>/', modificar_placa, name = "modificar_placa"),
    path('modificar_tarjeta/<id>/', modificar_tarjeta, name = "modificar_tarjeta"),
    path('eliminar_proce/<id>/', eliminar_proce, name = "eliminar_proce"),
    path('eliminar_tarjeta/<id>/', eliminar_tarjeta, name = "eliminar_tarjeta"),
    path('eliminar_placa/<id>/', eliminar_placa, name = "eliminar_placa"),
]