# -*- coding: UTF-8 -*-


class Cliente(object):
    """
    Classe cliente
    """

    def __init__(self, nome, cep, n_casa, lim_credito, status="Medio"):
        self.nome = nome
        self.cep = cep
        self.n_casa = n_casa
        self.lim_credito = lim_credito
        self.status = status

        
