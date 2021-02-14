def load_file(path):
  # TODO: borrar esto cuando se haga la implementacion posta
  with open(path, "rb") as data_file:
    return data_file.read()

class CovidSurvey:
  def __init__(self):
    self._answers = {}

  """
    La idea es para agregarle un toque de realidad al sistema
    que se genere un .json similar al covid_ddjj.example.json
    con preguntas por stdin al usuario/paciente
  """
  def run(self):
    # TODO: hacerlo posta en lugar de cargar el ejemplo
    return load_file("ddjj.example.json")
