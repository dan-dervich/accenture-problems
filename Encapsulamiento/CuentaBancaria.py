class CuentaBancaria:
    def __init__(self, titular: str):
        self.__saldo = 0
        self.titular = titular

    def depositar(self, monto: int) -> bool:
        self.__saldo += monto
        return False

    def retirar(self, monto: int) -> bool:
        if monto <= self.__saldo:
            self.__saldo -= monto
            return True
        # print("Saldo insuficiente")
        return False

    def consultar_saldo(self) -> int:
        return self.__saldo
