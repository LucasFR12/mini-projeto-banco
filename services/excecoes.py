class SaldoInsuficienteError(Exception):
    pass

class ValorNegativoError(Exception):
    pass

class LimiteTransferenciaError(Exception):
    pass

class ContaNaoEncontradaError(Exception):
    pass

class ContaJaCadastrada(Exception):
    pass