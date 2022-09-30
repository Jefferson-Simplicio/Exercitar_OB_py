from Agencia import AgenciaComun, Agencia, AgenciaVirtual, AgenciaPremiun
from ContasBancos import ContaCorrente, CartaoCredito

agenciap = AgenciaPremiun(48288688,15885564865316454)
agenciap.cadastrar_cliente('Jefferson', '145.098.639-00', 1000000000000)
print(agenciap.clientes)