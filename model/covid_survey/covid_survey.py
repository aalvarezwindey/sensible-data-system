import json

KEY_TEMPERATURE = 'temperatura'
KEY_DRY_COUGH = 'tos_seca'
KEY_LOSS_OF_SMELL = 'perdida_del_olfato'
KEY_LOSS_OF_TASTE = 'perdida_del_gusto'

DEFAULT_BOOLEAN_QUESTION = 'n'

class CovidSurvey:
  def __init__(self):
    self._answers = {}

  def run(self):
    self._answers[KEY_TEMPERATURE] = float(input('Indique su temperatura: '))
    self._answers[KEY_DRY_COUGH] = input('¿Posee tos seca? [s/N]: ') or DEFAULT_BOOLEAN_QUESTION
    self._answers[KEY_LOSS_OF_SMELL] = input('¿Ha perdido el olfato? [s/N]: ') or DEFAULT_BOOLEAN_QUESTION
    self._answers[KEY_LOSS_OF_TASTE] = input('¿Ha perdido el gusto? [s/N]: ') or DEFAULT_BOOLEAN_QUESTION
    return json.dumps(self._answers).encode("utf-8")
