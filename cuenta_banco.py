class CuentaBanco:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def deposito_cuenta(self, monto: float):
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser numérico")

        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")

        self.saldo += monto

    def retiro_cuenta(self, monto: float):
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser numérico")

        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")

        if monto > self.saldo:
            raise ValueError("Saldo insuficiente")

        self.saldo -= monto

    def transferencia_cuenta(self, monto: float, cuenta_destino):
        if not isinstance(cuenta_destino, CuentaBanco):
            raise TypeError("La cuenta destino no es válida")

        self.retiro_cuenta(monto)
        cuenta_destino.deposito_cuenta(monto)

    def saldo_cuenta(self) -> float:
        return self.saldo
