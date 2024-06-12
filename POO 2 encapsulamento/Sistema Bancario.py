class ContaBancaria:
    def __init__(self, titular, numero):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = 0

    def get_titular(self):
        return self.__titular

    def set_titular(self, novo_titular):
        self.__titular = novo_titular

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero_novo):
        self.__numero = numero_novo
        return numero_novo

    def get_saldo(self):
        return self.__saldo

    def __set_saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    def deposito(self, valor_deposito):
        if valor_deposito == 0:
            print("ERRO: Voce nao esta depositando nada")
            return
        elif valor_deposito < 0:
            print("ERRO: valor negativo")
            return
        else:
            self.__set_saldo(valor_deposito + self.get_saldo())
            return

    def saque(self, valor_saque):
        if valor_saque < 0:
            print("ERRO: Valor negativo")
            return
        elif self.get_saldo() < valor_saque:
            print("Saldo insuficiente")
            return
        else:
            self.__set_saldo(self.get_saldo() - valor_saque)
