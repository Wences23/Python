def  inicio de sesión ():
    # Pide al usuario que ingrese su nombre de usuario y contraseña
    nombreusuario  =  input ( "Introduce tu nombre de usuario: " )
    password  =  input ( "Introduce tu contraseña: " )

    # Aquí podrías hacer una consulta a una base de datos o leer un archivo con 
    # los datos de usuario y contraseña
    # En este ejemplo, simplemente se usan valores predefinidos para hacer la 
    # comprobacion
    si  nombre de usuario  ==  "usuario"  y  contraseña  ==  "contraseña" :
        print ( "Inicio de sesion exitosa" )
        volver  verdadero
    más :
        print ( "Nombre de usuario o contraseña incorrecta" )
        volver  falso