# -*- coding: utf-8 -*-
"""daily_serie.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ptjzSkcmQIGZvNOyHM3sp3ydw48hJ_yB
"""

!pip install hydrobr
import pandas as pd
import hydrobr as hb

class DailySerie(pd.DataFrame):
  """
  Serie de alturas pluviométricas diárias de uma estação.
  """

  def get_waterYear(self):
    ...

  def get_monthlyAvarege(self):

    """ calcula a média de cada mês de cada ano e filtra pelos valores calculados
    a partir de meses sem falhas (objetivando não influenciar na média final)"""

    serie_completa = self.resample('M').mean()
    meses_completos = self.resample('M').count()
    index_meses_completos = meses_completos[meses_completos[self.columns[0]]==self.resample('M').size()].index
    serie_filtrada = serie_completa.loc[index_meses_completos]

    #calcula a média mensal de toda a série
    media_mensal = serie_filtrada.groupby([serie_filtrada.index.month]).mean()

    return media_mensal.plot(kind='bar',figsize = (15,5))

  def get_anualMax(self):
    result = self.resample('Y').max()
    return result.plot(kind = 'bar', figsize = (15,5))

  def get_monthlyMax(self):
    result = self.resample('M').max()
    return result.plot( figsize = (15,5))

  def get_missingValues(self):

    """
    Fornece um dataframe com 12 colunas representando os meses de janeiro a
    dezembro e linhas representando cada ano da série e para cada mês calcula o
    número de falhas naquele mês/ano.
    """
    ...

