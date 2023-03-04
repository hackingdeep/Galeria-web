# Galeria-web
Para ejecutar el proyecto primero debe clonarlo con git clone  https://github.com/hackingdeep/Galeria-web.git en tu terminal,
luego de haber clonado el proyecto proceda a crear la base de datos para crear sus tablas con las migraciones 
para esto tiene dos opciones:

1- En el archivo settings.py se encuentra la configuración a la base de datos MYSQL donde solo tiene que agregar 
su nombre de base de datos, el usuario de la base de datos, su contraseña, su localhost y el puerto de MYSQL

Ejemplo: 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': NAME_BASE,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

luego en su terminal ejecute python manage.py makemigrations y despues python manage.py migrate,listo ahora puede ejecutar el proyecto con python manage.py runserver

2- Puede solo comentar la conexión de MYSQL Y descomentar la de SQLITE,luego ejecute el siguiente comando python manage.py runserver con eso ya podria ver la aplicación
ya que se va a generar un archivo sqlite por si solo cuando ejecute el comando mencionado, si le llega a pedir que ejecute las migraciones solo haga lo siguiente
python manage.py makemigrations y despues python manage.py migrate y listo
