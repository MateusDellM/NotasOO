

class conta_corrente:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


    def extrato(self):
        print("saldo {} do titular {}".format(self.saldo, self.titular))

