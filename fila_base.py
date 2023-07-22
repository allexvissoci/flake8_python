import abc
from typing import List
from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = TAMANHO_PADRAO_MINIMO
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ''

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
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
