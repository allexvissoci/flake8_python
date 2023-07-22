import abc


class FilaBase(metaclass=abc.ABCMeta):
    codigo = 0
    fila: list = []
    clientes_atendidos: list = []
    senha_atual = None

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def inserir_cliente(self) -> None:
        self.fila.append(self.senha_atual)

    @abc.abstractmethod
    def gera_senha_atual(self) -> None:
        ...

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.inserir_cliente()

    @abc.abstractmethod
    def chama_cliente(self, caixa: int) -> list:
        ...
