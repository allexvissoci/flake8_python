from typing import List, Dict, Union


class EstatisticaResumida:
    def __init__(self, dia, agencia) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: List[str]) -> dict:
        estatistica: Dict[str, Union[str, int, List[str]]] = {}
        estatistica[f'{self.agencia} - {self.dia}'] = len(clientes_atendidos)

        return estatistica
