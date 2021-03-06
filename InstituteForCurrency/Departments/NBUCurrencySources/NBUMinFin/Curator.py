# -- coding: utf-8 --
from __future__ import unicode_literals
from InstituteForCurrency.Departments.NBUCurrencySources.NBUMinFin.NBUUSD import NBUUSD
from InstituteForCurrency.Departments.NBUCurrencySources.NBUMinFin.NBUEUR import NBUEUR
from Memento.InstituteForCurrency.Departments.NBU_Currency import NBUCuratorMemento


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class MinFinCurator(NBUCuratorMemento):
    def __init__(self, chrono):
        self.__usd = NBUUSD(source=self._get_one_obj({'currency': 'USD'})['minfin_usd'], chrono=chrono)
        self.__eur = NBUEUR(source=self._get_one_obj({'currency': 'EUR'})['minfin_eur'], chrono=chrono)
        # self.__pln = BankPLN(source=self.get_one_obj({'currency': 'PLN'})['minfin_pln'], chrono=chrono)

        self.__directions = {'USD': self.__usd.appeal,
                             'EUR': self.__eur.appeal,
                             }

    def answer_from_curator(self):
        ...

    def question_to_curator(self, question):
        answer_to_departament = {}
        for key, value in question.items():
            answer_to_departament[key] = self.__directions[key](value)
        return answer_to_departament


if __name__ == '__main__':
    from Arsenal.Chronometer import Chronometer

    chronometer = Chronometer()
    chronometer.start()
    minfin = MinFinCurator(chronometer)
