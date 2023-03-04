from django.shortcuts import render, redirect, HttpResponse
from .models import Categoria, Foto
from .forms import MyUserCreationForm,PerfilForm
from .models import Userr
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home.html')


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('nombre')
        password = request.POST.get('contraseña')
        
        try:
            usuario = Userr.objects.get(username=username)
        except:
            messages.add_message(request=request,level=messages.ERROR,message='Nombre o Contraseña incorrecto')

        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            messages.add_message(request=request,level=messages.SUCCESS,message='A iniciado sesión correctamente')
            return redirect('perfil')
                 
    return render(request, 'iniciar_sesion.html')


def registro_usuario(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2'] and len(request.POST['password1']) >= 6:
            
            try:
                usuario = MyUserCreationForm(request.POST)
                usuario = Userr.objects.create_user(username=request.POST['username'],
                                                   password=request.POST['password1'])
                usuario.save()
                messages.add_message(request=request,level=messages.SUCCESS,message='Enhorabuena! te haz registrado exitosamente')
                return redirect('iniciar_sesion')
            except:
                return HttpResponse('error interno')

        else: 
          messages.add_message(request=request,level=messages.ERROR,message='La contraseña debe contener minimo 7 caracteres')
          return redirect('registro_usuario')
         
    
    else:
        return render(request, 'registrar_usuario.html', {'form':MyUserCreationForm() })


@login_required(login_url='iniciar_sesion')
def eliminar_usuario(request, id):
    usuario = Userr.objects.get(id=id)
    usuario.delete()
    return redirect('/')


@login_required(login_url='iniciar_sesion')
def eliminar_foto(request, id):
    foto = Foto.objects.get(id=id)
    foto.delete()
    return redirect('galeria')


@login_required(login_url='iniciar_sesion')
def eliminar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('galeria')


def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'fotos/lista_de_categorias.html', {'categorias': categorias})


@login_required(login_url='iniciar_sesion')
def galeria(request):
   
    categoria = request.GET.get('categoria')
    if categoria == None:
        fotos = Foto.objects.all()
    else:
        fotos = Foto.objects.filter(categoria__nombre__contains=categoria)
    
    categoria = Categoria.objects.all()
    usuario = request.user
    avatar_user = Userr.objects.filter(username=usuario)
    
    
    contexto = {'categorias': categoria, 
                'fotos': fotos,
                'avatar_user':avatar_user,
                }
    
    return render(request, 'fotos/galeria.html', contexto)


@login_required(login_url='iniciar_sesion')
def ver_foto(request, id):
    fotos = Foto.objects.get(id=id)
    fotoss = Foto.objects.all()
    return render(request, 'fotos/foto.html', {'fotos': fotos, 'fotoss': fotoss})


@login_required(login_url='iniciar_sesion')
def agregar_foto(request):
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        datos = request.POST
        usuario = request.user
        imagen = request.FILES.get('imagen')

        if datos['categoria'] != 'none':
            categoria = Categoria.objects.get(id=datos['categoria'])
        elif datos['categoria_nueva'] != '':
            categoria, crear = Categoria.objects.get_or_create(
                nombre=datos['categoria_nueva'],usuario=usuario)
        else:
            categoria = None

        foto = Foto.objects.create(
            categoria=categoria,
            descripcion=datos['descripcion'],
            imagen=imagen,
            usuario=usuario
        )

        return redirect('galeria')
    contexto = {'categorias': categorias}
    return render(request, 'fotos/agregar.html', contexto)


@login_required(login_url='iniciar_sesion')
def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion')


# cambiar contraseña de usuario, me destruye la sesión y no se como resolver lo :C
# @login_required(login_url='iniciar_sesion')
# def cambiar_contraseña(request, id):
#     contraseña = request.POST.get('contraseña')
#     user = Userr.objects.get(id=id)
#     user.set_password(contraseña)
#     user.save()
#     return render(request, 'cambiar_contraseña.html')


@login_required(login_url='iniciar_sesion')
def perfil_usuario(request):
    usuario = request.user
    mostrar_datos_perfil = Userr.objects.filter(username=usuario)

    fotos=Foto.objects.filter(usuario=usuario).count()
    fotoss = Foto.objects.filter(usuario=usuario).all()[0:4]
    
    categorias = Categoria.objects.all()
    contexto = {'fotos':fotos,'categorias':categorias,
                'mostrar_datos_perfil':mostrar_datos_perfil,
                'usuario':usuario,
                'fotoss':fotoss
               }
    
    return render(request, 'perfil.html',contexto)



@login_required(login_url='iniciar_sesion')
def Actualizar_Perfil(request,id):
    
    foto_perfil = Userr.objects.filter(username=request.user)
    user = Userr.objects.get(id=id)

    formu = PerfilForm(instance=user)
    print(request.POST)
    if request.method == 'POST':
        formu = PerfilForm(request.POST, request.FILES, instance=user)
        if formu.is_valid():
            formu.save()
            return redirect('perfil')

    return render(request, 'actualizar_Perfil.html', {'formu': formu,
                                                    'usuario': user,
                                                    'foto_perfil':foto_perfil})

