import yaml
import os
import shutil
import subprocess
import lib


def cprint(s: str):
    print('[UC]\t' + s)


cprint('loading config files...')
with open(lib.abs_path(f'config{os.sep}general.yaml'), 'r', encoding='UTF-8') as in_stream:
    config_loaded = yaml.safe_load(in_stream)
migrator_path = lib.abs_path(config_loaded['cobalt migrator path'])
with open(lib.abs_path(f'config{os.sep}cobalt_update.yaml'), 'r', encoding='UTF-8') as in_stream:
    config_loaded = yaml.safe_load(in_stream)
romfs_path = lib.abs_path(config_loaded['romfs mod directory path'])
cobalt_path = lib.abs_path(config_loaded['cobalt mod directory path'])
cobalt_direct_path = lib.abs_path(config_loaded['cobalt direct path']) if 'cobalt direct path' in config_loaded else ''
cprint('updating to romfs...')
p = subprocess.Popen('update_to_romfs.exe')
p.wait()
mod_name = os.path.basename(romfs_path)
migrated_path = cobalt_path + os.sep + mod_name + ' (Cobalt)'
if os.path.exists(migrated_path) and os.path.isdir(migrated_path):
    cprint(f'deleting \"{migrated_path}\"')
    shutil.rmtree(migrated_path)
argv_line = [migrator_path, romfs_path]
subprocess.Popen(argv_line, cwd=cobalt_path).wait()
if cobalt_direct_path:
    cprint('Directly copying...')
    shutil.copytree(cobalt_direct_path, os.path.join(migrated_path, 'patches'), dirs_exist_ok=True)
    cprint('Done')
else:
    cprint('Nothing to be copied')
