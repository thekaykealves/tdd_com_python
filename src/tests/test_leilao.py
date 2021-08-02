from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.kaka = Usuario("Kaka", 500.0)
        self.lance_do_kaka = Lance(self.kaka, 150.0)
        self.leilao = Leilao("Celular")

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        andre = Usuario("André", 500.0)
        lance_do_andre = Lance(andre, 100.0)

        self.leilao.propoe(lance_do_andre)
        self.leilao.propoe(self.lance_do_kaka)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            andre = Usuario("André", 500.0)
            lance_andre = Lance(andre, 100.0)

            self.leilao.propoe(self.lance_do_kaka)
            self.leilao.propoe(lance_andre)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_kaka)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        andre = Usuario("André", 500.0)
        lance_andre = Lance(andre, 100.0)
        maria = Usuario("Maria", 500.0)
        lance_maria = Lance(maria, 200.0)

        self.leilao.propoe(lance_andre)
        self.leilao.propoe(self.lance_do_kaka)
        self.leilao.propoe(lance_maria)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tiver_lances(self):
        self.leilao.propoe(self.lance_do_kaka)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        andre = Usuario("André", 500.0)
        lance_do_andre = Lance(andre, 200.0)

        self.leilao.propoe(self.lance_do_kaka)
        self.leilao.propoe(lance_do_andre)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebido)

    def test_nao_deve_permitir_propor_um_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_kaka_de_200 = Lance(self.kaka, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_kaka)
            self.leilao.propoe(lance_do_kaka_de_200)