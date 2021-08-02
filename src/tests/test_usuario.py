from src.leilao.dominio import Usuario, Leilao
import pytest

from src.leilao.excecoes import LanceInvalido


@pytest.fixture
def kaka():
    return Usuario('Kaka', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(kaka, leilao):
    kaka.propoe_lance(leilao, 50.0)

    assert kaka.carteira == 50.0


def test_deve_permitir_propor_um_lance_se_o_valor_for_menor_do_que_o_valor_da_carteira(kaka, leilao):
    kaka.propoe_lance(leilao, 1.0)

    assert kaka.carteira == 99.0


def test_deve_permitir_propor_um_lance_quando_o_valor_for_igual_o_valor_da_carteira(kaka, leilao):
    kaka.propoe_lance(leilao, 100.0)

    assert kaka.carteira == 0.0

def test_nao_deve_permitir_um_lance_com_valor_maior_do_que_o_valor_da_carteira(kaka, leilao):
    with pytest.raises(LanceInvalido):

        kaka.propoe_lance(leilao, 200.0)
