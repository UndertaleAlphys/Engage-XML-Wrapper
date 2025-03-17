import yaml
import os
import sys
import subprocess
import lib

# load general config file - get engage_xml path and output path
with open(lib.abs_path(f'config{os.sep}general.yaml'), 'r', encoding='UTF-8') as in_stream:
    config_loaded = yaml.safe_load(in_stream)
engage_xml_path = lib.abs_path(config_loaded['engage xml path'])
# parse the bundles one by one - to xlsx, to the output path
for file in sys.argv:
    arg_line = [engage_xml_path, lib.abs_path(file)]
    subprocess.Popen(arg_line)