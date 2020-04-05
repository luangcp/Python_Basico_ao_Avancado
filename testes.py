import unittest

from atividades import comer, dormir, eh_engracada


class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudavel."""
        self.assertEqual(
            comer('quiabo', True),  # podemos ou n usar parametros nomeados
            'Estou comendo quiabo, porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comida não saudavel."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),  # podemos ou n usar parametros nomeados
            'Estou comendo pizza, porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando o retorno com dormi pouco."""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas.'
        )

    def test_dormir_muito(self):
        """Testando o retorno com dormi muito."""
        self.assertEqual(
            dormir(10),
            'PUTZ! Dormi muito! estou atrasado para o trabalho!'
        )

    def test_eh_engracada(self):
        """Testando o retorno de é engraçada"""
        # self.assertEqual(eh_engracada('Sérgio Malandro'), False)
        self.assertFalse(eh_engracada('Sérgio Malandro'))  # queremos que o resultado seja falso
        self.assertTrue(eh_engracada('Luan'), 'Luan deveria ser engraçado')


if __name__ == '__main__':
    unittest.main()