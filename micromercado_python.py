#Derrollo del inventario

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
    'PRODUC15': ['CREMA DE LECHE : 300ML', 9.00, 14],
    
    # --- BEBIDAS Y JUGOS ---
    'PRODUC16': ['GASEOSA : 2L', 11.50, 30],
    'PRODUC17': ['AGUA MINERAL : 2L', 5.00, 25],
    'PRODUC18': ['JUGO EN CAJA : 1L', 7.50, 20],
    
    # --- ENLATADOS Y CONSERVAS ---
    'PRODUC19': ['ATÚN EN LATA : 170G', 8.50, 35],
    'PRODUC20': ['SARDINA EN LATA : 425G', 12.00, 18],
    'PRODUC21': ['EXTRACTO DE TOMATE : 140G', 3.50, 25],
    'PRODUC22': ['MAÍZ EN LATA : 300G', 6.00, 15],
    
    # --- SNACKS Y CONFITERÍA ---
    'PRODUC23': ['PAPAS FRITAS : 100G', 6.50, 30],
    'PRODUC24': ['GALLETAS SALADAS : 3 PACKS', 4.00, 28],
    'PRODUC25': ['GALLETAS DULCES : 150G', 3.50, 35],
    'PRODUC26': ['CHOCOLATE : 100G', 9.00, 20],
    'PRODUC27': ['CEREAL : 500G', 22.00, 10],
    
    # --- HIGIENE Y ASEO PERSONAL ---
    'PRODUC28': ['PAPEL HIGIÉNICO : 4 ROLLOS', 7.50, 45],
    'PRODUC29': ['CHAMPÚ : 400ML', 25.00, 12],
    'PRODUC30': ['PASTA DENTAL : 90G', 11.00, 18],
  
    
    # --- LIMPIEZA DEL HOGAR ---
    'PRODUC31': ['DETERGENTE ROPA : 1KG', 15.00, 20],
    'PRODUC32': ['LAVAVAJILLAS LÍQUIDO : 500ML', 8.50, 22],
    'PRODUC33': ['ESPONJA DE COCINA : 3 UNID', 3.50, 40],
    
    # --- PANADERÍA Y OTROS ---
    'PRODUC34': ['PAN DE MOLDE : 500G', 10.50, 12],
    'PRODUC35': ['MERMELADA : 250G', 9.00, 16],

}



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
                ---------------------------------------
                PANEL DE CONTROL DE VENTAS MICROMERCADO
                ---------------------------------------
                1. Ver Inventario de Productos
                2. Realizar una Venta
                3. Aumentar Stock
                4. Volver al menú principal
                ''')
                opcion_micromercado = int(input('Ingrese su opcion: '))

                if opcion_micromercado ==1:
                    print('INVENTARIO DE PRODUCTOS')
                    print("\n" + "="*58)
                    print(f"{'Código':<10} | {'Producto':<25} | {'Precio':<8} | {'Stock':<6}")
                    print("-" * 58)

                    for cod, datos in inventario.items():
                        nombre_productos = datos[0][0:25]

                        print(f"{cod:<10} | {nombre_productos:<25} | ${datos[1]:<7.2f} | {datos[2]:<6}")
                    print("="*58)
        #Codigo realizado para la opcion de Realizar una venta
                if opcion_micromercado ==2:

                    carrito =[]         # Esta variable se usará para almacenar los productos registrados    
                    total_venta = 0     # esta variable servirá para acumular el total del dinero para pagar.

                    print ('''
                    -----------------------------------
                           Nueva Venta - RONSISTEM
                    -----------------------------------
                            ''')
                    print('Escriba (FINALIZAR VENTA) para terminar la venta')

                    while True:
                        buscar_codigo = input('Ingrese el Código del Próducto: ').strip().upper()

                        if buscar_codigo == 'FINALIZAR VENTA':
                            break
                        if buscar_codigo in inventario:
                            datos_producto = inventario[buscar_codigo] #Esto sirve para buscar y visualizar la lista del diccionario (inventario) [nombre, precio. stock]
                            nombre = datos_producto[0]
                            precio = datos_producto[1]
                            stock_actual = datos_producto[2]

                        # En esta parte o bloque de codigo se creó para saber si hay disponible el producto en el diccionario INVENTARIO de productos.
                            if stock_actual > 0:
                                print(f'Producto: {nombre}, | Precio: Bs {precio: .2f} | Stock: {stock_actual} ')
                                cantidad = int(input(f'¿Que cantidad registrarás?: '))

                                if cantidad <= 0:
                                    print('¡La cantidad que debe registrar debe ser mínimo de 1 producto. Intente de nuevo!') #Para que el usuario sí o sí registre una cantidad del producto
                                elif cantidad <= stock_actual:
                                    inventario [buscar_codigo][2] -= cantidad #Acá se reduce o resta la cantidad de stock de los productos

                                    subtotal = precio * cantidad
                                    total_venta += subtotal           #Acá se calcula el subtoral del producto 

                                    #Acá usaremo un nuevo método "append()" para guardar o agregar  en la varible carrito que es una lista y así hacer visible el producto registrado.
                                    carrito.append (f'{nombre} ||{cantidad} || {subtotal}')
                                    print(f'Se añadió correctamente el  producto: {nombre}, en una cantidad de: {cantidad}, por un precio de: {subtotal:.2f}')
                                else:
                                    print(f' No hay suficiente de este. producto en Stock. Solo quedan {stock_actual} unidades disponibles')
                            else:
                                print('El código que ingresó no existe. Intente de nuevo por favor.')

                        if len(carrito)>0:                 #Este bloque visualiza el ticket de compra realizado             
                            print('''
                                    --------------------------------------
                                        DETALLE DE LA VENTA REALIZADA
                                    --------------------------------------
                                    ''')
                            print(f'{'Detalle Producto':<25} | {'Cantidad':<5} | {'Total':<8}')
                            print('-' * 45)

                            for item in carrito:
                                partes = item.split('||')
                                produc_nombre = partes[0][0:25] #uso del slicing 
                                produc_cant = partes [1]
                                product_subtotal = float(partes[2]) #usamos para dos decimales

                                print (f'{produc_nombre:<25} | {produc_cant:<5} | {product_subtotal:<8.2f}') 

                            print ('-' * 45)
                            print(f'TOTAL A PAGAR< {''<14} Bs {total_venta: .2f}')
                            print ('-' * 45)
                            input('Presione ENTER para regresar al menú PANEL DE CONTROL DE VENTAS')


              # elif opcion_micromercado == 3:
                    #Acá trabajaremos la opción de recargar el stock de productos





        #Codigo realizado para la opcion de Volver al Menú principal
                elif opcion_micromercado == 4:
                    print(f'Usted {usuario.upper()} volviendo al menú principal...')
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








