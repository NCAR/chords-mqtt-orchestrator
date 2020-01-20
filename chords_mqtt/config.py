import os
import shutil
from pathlib import Path

import yaml

original_config_file = os.path.join(os.path.dirname(__file__), 'config.yaml')

config_dir = Path('~/chords_mqtt').expanduser()
config_dir.mkdir(exist_ok=True, parents=True)

config_file = config_dir / 'config.yaml'

if not config_file.exists():
    print(original_config_file, config_file)
    shutil.copyfile(original_config_file, config_file)


with open(f'{config_dir}/config.yaml') as f:
    config = yaml.safe_load(f)
