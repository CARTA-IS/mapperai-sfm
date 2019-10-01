import json

from opensfm import context

from opensfm import io

with io.open_rt(context.SENSOR) as f:
    sensor_data = io.json_load(f)

# Convert model types to lower cases for easier query
sensor_data = dict(zip(map(lambda x:x.lower(),sensor_data.keys()),sensor_data.values()))

