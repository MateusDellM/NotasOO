class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        #self.__codigo_banco = "002" ---- não é nececssario, metodo statico


    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))


    def deposita(self, valor):
        self.__saldo += valor


    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_para_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_para_sacar


    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= self.limite
        else:
            print("O valor passou o limite".format(valor))


    def tranfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property #usado com metodo de GET, para atributos "privados"
    def limite(self):
        return self.__limite

    @limite.setter #usado como metodo SET...
    def set__limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return  "002"