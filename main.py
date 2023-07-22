# from fila_normal import FilaNormal
# # from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
# from estatistica_resumida import EstatisticaResumida
from constantes import TIPO_FILA_PRIORITARIA


# # fila_teste = filanormal()
# # fila_teste.atualizafila()
# # fila_teste.atualizafila()
# # fila_teste.atualizafila()
# # fila_teste.atualizafila()
# # print(fila_teste.chamacliente(5))
# # print(fila_teste.chamacliente(10))

# fila_teste_2 = FilaNormal()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# print(fila_teste_2.chama_cliente(10))
# # print(fila_teste_2.estatistica('10/01/1993', 197, 'detail'))

fabrica_fila = FabricaFila.pega_fila(TIPO_FILA_PRIORITARIA)
fabrica_fila.atualiza_fila()
fabrica_fila.atualiza_fila()
fabrica_fila.atualiza_fila()
print(fabrica_fila.chama_cliente(10))
print(fabrica_fila.chama_cliente(10))
print(fabrica_fila.chama_cliente(10))
print(fabrica_fila.estatistica(EstatisticaDetalhada('10/01/1993', 197)))
