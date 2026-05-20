
#Desarrollo en entrada de inputs

usuario_creacion = input("Cree su usuario, con mínimamente 8 caracteres: ")
while len(usuario_creacion) <8:
    print("Su nombre de usuario debe tener mínimamente 8 caracteres")
    usuario_creacion = input('Su usuario debe tener 8 caracteres. Intente de nuevo: ')
else:
    print("""
          ------------------------------------------------
          Usuario creado correctamente, creando usuario... 
          ------------------------------------------------""")

# desarrollo de la opción de 3 intentos, si ingresa el usuario ingresa de forma incorrecta

intentos = 3

acceso_concedido = False

while intentos > 0:
    usuario = input(f"Ingrese su usuario: Usted tiene : {intentos} intentos: ")
    if usuario_creacion == usuario:
        print('Usuario correcto: Acceso al sistema >>> verificado>>>>')
        acceso_concedido = True
        break
    else:
        intentos -= 1
        print(f'Usuario Incorrecto')


# Desarrollo del verificador de acceso en caso de intentos errados

if acceso_concedido == True:
    print ('Bienvenido al sistema de ventas de MICROMERCADO: RONSISTEM')
else:
    print('Su número de intentos terminaron: Bloqueo de sistema RONSISTEM')
