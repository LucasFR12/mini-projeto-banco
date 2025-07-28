from services.excecoes import ValorNegativoError, SaldoInsuficienteError, ContaNaoEncontradaError


class ContaBancaria:


    def __init__(self, nome, senha, saldo=0.0):
        self._nome = nome
        self._senha = senha
        self._saldo = saldo

    @property
    def nome(self):
        return self._nome
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha
    
    def sacar(self, valor_saque):
        if valor_saque < 0:
            raise ValorNegativoError(f"Não é possível sacar um valor negativo!")
        elif valor_saque > self.saldo:
            raise SaldoInsuficienteError(f"Saldo insuficiente! Saldo Atual: R${self.saldo}")
        else:
            self._saldo -= valor_saque

    def depositar(self, valor_deposito):
        if valor_deposito < 0:
            raise ValorNegativoError(f"Não é possível depositar um valor negativo!")
        else:
            self._saldo += valor_deposito

    def transferir(self, valor, conta_destino):
        if not conta_destino:
            raise ContaNaoEncontradaError(f"Conta: '{conta_destino.nome.upper()}' não encontrada!")
        elif valor < 0:
            raise ValorNegativoError(f"Não é possível transferir um valor negativo!")
        elif valor > self.saldo:
            raise SaldoInsuficienteError(f"Saldo insuficiente! Saldo Atual: R${self.saldo}")
        else:
            self._saldo -= valor
            conta_destino.depositar(valor)

    def exibir_info(self):
        print(f"Nome: {self.nome} | Saldo: R$ {self.saldo} | Senha: {self.senha}")
    
    def __str__(self):
        return f"Nome: {self.nome} | Saldo: {self.saldo}"
    
    def to_dict(self):
        return {"nome": self.nome, "saldo": self.saldo, "senha":self.senha}
    
    @staticmethod
    def from_dict(dados):
        return ContaBancaria(dados["nome"], dados["senha"], dados["saldo"])
        