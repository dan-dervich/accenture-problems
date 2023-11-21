class CuentaBancaria:
    def __init__(self, titular: str):
        self.__saldo = 0
        self.titular = titular

    def depositar(self, monto: int):
        self.__saldo += monto

    def retirar(self, monto: int):
        if monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Saldo insuficiente")

    def consultar_saldo(self):
        return self.__saldo
