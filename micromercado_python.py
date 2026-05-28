
#Desarrollo de inputs

# Variables para recordar los datos al cambiar de opción

usuario_creacion = "ronald.ricaldi"
password_creacion = "1234"
acceso_concedido = False

while True:
    print('''   
        -----------------------------------------
        Bienvenido al sistema de ventas RONSISTEM
        -----------------------------------------
            ''')
    print('¿Qué procedimiento desea realizar?\n')

    opcion = int(input('''      
        1. Crear Nuevo Usuario
        2. Iniciar Sesión
        3. Salir del sistema
        
        Ingrese su opción: '''))

    # OPCIÓN 1: CREAR USUARIO
    
    if opcion == 1:
        
        usuario_creacion = input("Cree su usuario (mínimamente 8 caracteres): ").strip()
        
        while len(usuario_creacion) < 8:
            print("Su nombre de usuario debe tener mínimamente 8 caracteres.")
            usuario_creacion = input('Intente de nuevo: ').strip()
        else:
            print("""
            ------------------------------------------------
                    ¡Usuario creado correctamente! 
            ------------------------------------------------
                """)
            
            
            password_creacion = input('Cree su password (debe tener exactamente 4 dígitos): ').strip()
            
            while len(password_creacion) != 4:
                print('Su password debe tener exactamente 4 dígitos.')
                password_creacion = input('Intente de nuevo: ').strip()
            else:
                print('''
            -------------------------------
            ¡Password creado correctamente!
            -------------------------------
                ''')
        
                    
    # OPCIÓN 2: INICIAR SESIÓN 

    elif opcion == 2:
        intentos = 3
        print(">>>>INICIO DE SESIÓN>>>>>")
        
        while intentos > 0:
            usuario = input(f"Ingrese su usuario (Tiene {intentos} intentos): ").strip()
            password = input("Ingrese su contraseña: ").strip()
            
            # Validacion de ambos datos para que coincidan
            if usuario == usuario_creacion and password == password_creacion:
                
                print(f'Usuario correcto: Acceso al sistema >>> {usuario.upper()} VERIFICADO >>>>')
                acceso_concedido = True
                break
            else:
                intentos -= 1
                print(f'Datos incorrectos. Le quedan {intentos} intentos.\n')

        # Desarrollo del verificador de acceso y menu scundario interno
        if acceso_concedido == True:
            print(f'Bienvenido al sistema de ventas de MICROMERCADO: RONSISTEM {usuario.upper()}')

            while True:
                print('''
                -----------------------------------
                    PANEL DE CONTROL MICROMERCADO
                -----------------------------------
                1. Ver Inventario de Productos
                2. Cerrar Sesión (Volver al menú principal)
                ''')
                opcion_micromercado = int(input('Ingrese su opcion: '))

                if opcion_micromercado ==1:
                    print('Acá se mostrará el INVENTARIO DE PRODUCTOS')

                elif opcion_micromercado == 2:
                    print(f'Usted {usuario.upper()} está cerrando sesión...')
                    acceso_concedido=False
                    break

        else:
            print('Su número de intentos terminaron: Bloqueo de sistema RONSISTEM')

        
        # OPCIÓN 3: SALIR
    elif opcion == 3:
            print('Usted salió del sistema de ventas RONSISTEM. ¡Hasta luego!')
            break

    else:
            print('Opción inválida. Reinicie el programa y elija 1, 2 o 3.')



inventario = {
    # --- ABARROTES Y BÁSICOS ---
    'PRODUC01': ['ARROZ : 1KG', 3.50, 25],
    'PRODUC02': ['FIDEO : 1KG', 2.50, 20],
    'PRODUC03': ['LECHE : 1L', 9.50, 35],
    'PRODUC04': ['QUESO : 1KG', 40.50, 15],
    'PRODUC05': ['ACEITE : 1L', 12.50, 30],
    'PRODUC06': ['AZÚCAR : 1KG', 4.00, 40],
    'PRODUC07': ['SAL : 1KG', 1.50, 15],
    'PRODUC08': ['HARINA : 1KG', 5.00, 25],
    'PRODUC09': ['CAFÉ : 250G', 18.00, 12],
    'PRODUC10': ['TÉ : 50 SOBRES', 6.50, 20],
    
    # --- LÁCTEOS Y EMBUTIDOS ---
    'PRODUC11': ['YOGURT : 1L', 11.00, 18],
    'PRODUC12': ['MANTEQUILLA : 250G', 8.50, 22],
    'PRODUC13': ['JAMÓN : 250G', 14.00, 10],
    'PRODUC14': ['SALCHICHA : 500G', 16.50, 15],
    'PRODUC15': ['HUEVOS : 30 UNID', 24.00, 8],
    'PRODUC16': ['CREMA DE LECHE : 300ML', 9.00, 14],
    
    # --- BEBIDAS Y JUGOS ---
    'PRODUC17': ['GASEOSA : 2L', 11.50, 30],
    'PRODUC18': ['AGUA MINERAL : 2L', 5.00, 25],
    'PRODUC19': ['JUGO EN CAJA : 1L', 7.50, 20],
    'PRODUC20': ['BEBIDA ENERGÉTICA : 350ML', 10.00, 15],
    'PRODUC21': ['CERVEZA : 620ML', 13.00, 24],
    
    # --- ENLATADOS Y CONSERVAS ---
    'PRODUC22': ['ATÚN EN LATA : 170G', 8.50, 35],
    'PRODUC23': ['SARDINA EN LATA : 425G', 12.00, 18],
    'PRODUC24': ['SOPA INSTANTÁNEA : 70G', 4.50, 40],
    'PRODUC25': ['EXTRACTO DE TOMATE : 140G', 3.50, 25],
    'PRODUC26': ['MAÍZ EN LATA : 300G', 6.00, 15],
    'PRODUC27': ['POROTOS EN LATA : 400G', 7.00, 12],
    
    # --- SNACKS Y CONFITERÍA ---
    'PRODUC28': ['PAPAS FRITAS : 100G', 6.50, 30],
    'PRODUC29': ['GALLETAS SALADAS : 3 PACKS', 4.00, 28],
    'PRODUC30': ['GALLETAS DULCES : 150G', 3.50, 35],
    'PRODUC31': ['CHOCOLATE : 100G', 9.00, 20],
    'PRODUC32': ['CHICLES : CAJA 12U', 5.00, 15],
    'PRODUC33': ['CEREAL : 500G', 22.00, 10],
    
    # --- HIGIENE Y ASEO PERSONAL ---
    'PRODUC34': ['PAPEL HIGIÉNICO : 4 ROLLOS', 7.50, 45],
    'PRODUC35': ['CHAMPÚ : 400ML', 25.00, 12],
    'PRODUC36': ['JABÓN DE TOCADOR : 3 UNID', 10.50, 20],
    'PRODUC37': ['PASTA DENTAL : 90G', 11.00, 18],
    'PRODUC38': ['DESODORANTE : 150ML', 22.50, 15],
    'PRODUC39': ['TOALLAS SANITARIAS : 8U', 8.00, 25],
    'PRODUC40': ['CEPILLO DE DIENTES : 1U', 6.50, 14],
    
    # --- LIMPIEZA DEL HOGAR ---
    'PRODUC41': ['DETERGENTE ROPA : 1KG', 15.00, 20],
    'PRODUC42': ['LAVAVAJILLAS LÍQUIDO : 500ML', 8.50, 22],
    'PRODUC43': ['LIMPIADOR LÍQUIDO : 1L', 7.00, 18],
    'PRODUC44': ['LAVANDINA / CLORO : 1L', 4.50, 30],
    'PRODUC45': ['ESPONJA DE COCINA : 3 UNID', 3.50, 40],
    'PRODUC46': ['BOLSAS DE BASURA : 10 UNID', 6.00, 25],
    
    # --- PANADERÍA Y OTROS ---
    'PRODUC47': ['PAN DE MOLDE : 500G', 10.50, 12],
    'PRODUC48': ['MERMELADA : 250G', 9.00, 16],
    'PRODUC49': ['DULCE DE LECHE : 250G', 11.50, 14],
    'PRODUC50': ['MAYONESA : 200G', 5.50, 25]
}





