__author__ = 'aymgal'

from coolest.template.classes.lensing_entity import LensingEntity
from coolest.template.classes.mass_light_model import MassModel, LightModel


class Galaxy(LensingEntity):

    def __init__(self,
                 name: str,
                 redshift: float,
                 light_model: LightModel = None,
                 mass_model: MassModel = None) -> None:
        super().__init__(name, redshift, mass_model=mass_model)
        if light_model is None:
            light_model = LightModel()
        self.light_model = light_model
