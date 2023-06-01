# Test script that creates a whole LensUniverse model
# emulating a series of inputs from e.g. a user interface,
# and finally write it on disk as YAML or JSON files.

from coolest.template.classes.mass_light_model import MassModel, LightModel
from coolest.template import info
from coolest.template.json import JSONSerializer

from pprint import pprint


# here we specify all API keys that should *not* be included in the JSON template
exclude_keys = [
    'id',
    'fixed',
    'initial_estimate',
    'point_estimate',
    'prior',
    'posterior_stats',
    'order_in_memory',
]


all_mass_profiles = MassModel(*info.all_supported_choices['mass_profiles'])
all_light_profiles = LightModel(*info.all_supported_choices['light_profiles'])

# pprint(all_mass_profiles)
# pprint(all_light_profiles)

# ENCODE IN JSON
encoder_json = JSONSerializer('all_mass_profiles', obj=all_mass_profiles, indent=2)
encoder_json.dump_simple(exclude_keys=exclude_keys)
encoder_json = JSONSerializer('all_light_profiles', obj=all_light_profiles, indent=2)
encoder_json.dump_simple(exclude_keys=exclude_keys)
