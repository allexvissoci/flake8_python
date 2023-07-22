from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from constantes import TIPO_FILA_PRIORITARIA

fabrica_fila = FabricaFila.pega_fila(TIPO_FILA_PRIORITARIA)
fabrica_fila.atualiza_fila()
fabrica_fila.atualiza_fila()
fabrica_fila.atualiza_fila()
print(fabrica_fila.chama_cliente(10))
print(fabrica_fila.chama_cliente(10))
print(fabrica_fila.chama_cliente(10))
print(fabrica_fila.estatistica(EstatisticaDetalhada('10/01/1993', 197)))
