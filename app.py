from cuenta_banco import CuentaBanco


def mostrar_menu():
    print("\n--- MENÚ BANCO ---")
    print("1. Depósito")
    print("2. Retiro")
    print("3. Transferencia")
    print("4. Consulta de saldo")
    print("5. Salir")


def main():
    cuenta_origen = CuentaBanco("Titular Principal", 1000.0)
    cuenta_destino = CuentaBanco("Cuenta Destino", 500.0)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                monto = float(input("Ingrese monto a depositar: "))
                cuenta_origen.deposito_cuenta(monto)
                print("Depósito realizado correctamente")

            elif opcion == "2":
                monto = float(input("Ingrese monto a retirar: "))
                cuenta_origen.retiro_cuenta(monto)
                print("Retiro realizado correctamente")

            elif opcion == "3":
                monto = float(input("Ingrese monto a transferir: "))
                cuenta_origen.transferencia_cuenta(monto, cuenta_destino)
                print("Transferencia realizada correctamente")

            elif opcion == "4":
                print(f"Saldo actual: S/ {cuenta_origen.saldo_cuenta():.2f}")

            elif opcion == "5":
                print("Gracias por usar el sistema")
                break

            else:
                print("Opción inválida")

        except (ValueError, TypeError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
