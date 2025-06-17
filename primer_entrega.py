# Diccionario
usuarios = {}

# Funcion para registrar un nuevo usuario
def registrar_usuario():
    print("\n--- Registro de nuevo usuario ---")
    print()
    usuario = input("Nombre de usuario: ").strip()
    if not usuario:
        print("El nombre de usuario no puede estar vacío.")
        return
    if usuario in usuarios:
        print("Este nombre de usuario ya está registrado.")
        return
    print("La contraseña debe cumplir con los siguientes requisitos:")
    print("- Más de 6 caracteres")
    print("- Contener números")
    print("- Contener letras")
    while True:
        contraseña = input("Contraseña: ").strip()
        if not contraseña:
            print("La contraseña no puede estar vacía.")
            continue
        if len(contraseña) <= 6:
            print("La contraseña debe tener más de 6 caracteres.")
            continue
        if not any(c.isalpha() for c in contraseña):
            print("La contraseña debe contener al menos una letra.")
            continue
        if not any(c.isdigit() for c in contraseña):
            print("La contraseña debe contener al menos un número.")
            continue
        break
    usuarios[usuario] = contraseña
    print("Usuario registrado con éxito.")

# Funcion para mostrar los usuarios registrados
def mostrar_usuarios():
    print("\n--- Lista de usuarios registrados ---")
    print()
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print(f"Total de usuarios registrados: {len(usuarios)}")
        for idx, usuario in enumerate(usuarios, 1):
            print(f"{idx}. {usuario}")
          

# Funcion para iniciar sesión
def login():
    print("\n--- Iniciar sesión ---")
    print()
    usuario = input("Nombre de usuario: ").strip()
    if not usuario:
        print("El nombre de usuario no puede estar vacío.")
        return
    contraseña = input("Contraseña: ").strip()
    if not contraseña:
        print("La contraseña no puede estar vacía.")
        return
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Usuario o contraseña incorrectos.")

# Funcion - Menu principal
def menu():
    while True:
        print("\n--- Menu ---")
        print()
        print("1. Registrar usuario")
        print()
        print("2. Iniciar sesión")
        print()
        print("3. Mostrar usuarios registrados")
        print()
        print("4. Salir")
        print()
        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            login()
        elif opcion == '3':
            mostrar_usuarios()
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta la proxima!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
menu()
