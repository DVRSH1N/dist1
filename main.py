from models.Climbers import Climbers
from models.Regons import Regons
from models.Mountains import Mountains
from models.Ascents import Ascents
from modelDB4.human import human
from modelDB4.incedent import incident
incident = incident()
human = human()
climber = Climbers()
region = Regons()
mountains = Mountains()
ascents = Ascents()


# incident.delete(2)
print(incident.get())









