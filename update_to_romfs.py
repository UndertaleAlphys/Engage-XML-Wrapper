import yaml
import os
import subprocess
import lib

with open(lib.abs_path(f'config{os.sep}general.yaml'), 'r', encoding='UTF-8') as in_stream:
    config_loaded = yaml.safe_load(in_stream)
engage_xml_path = lib.abs_path(config_loaded['engage xml path'])
with open(lib.abs_path(f'config{os.sep}romfs_update.yaml'), 'r', encoding='UTF-8') as in_stream:
    config_loaded = yaml.safe_load(in_stream)
ignored_exts = [ext.lower() for ext in config_loaded['ignored exts']]
input_dir = lib.abs_path(config_loaded['input directory path'])
output_dir = lib.abs_path(config_loaded['output directory path'])
subprocess_lst: list[subprocess.Popen] = []


def parse_recursively(in_path: str, out_path: str, executable_path: str, ignored: list[str],
                      subprocess_list: list[subprocess.Popen]):
    if not (os.path.exists(out_path) and os.path.isdir(out_path)):
        os.mkdir(out_path)
    for file in os.listdir(in_path):
        _, ext = os.path.splitext(file)
        if ext.lower() in ignored:
            continue
        abs_file = in_path + os.sep + file
        if os.path.isdir(abs_file):
            parse_recursively(abs_file, out_path + os.sep + file, executable_path, ignored, subprocess_list)
        else:
            out_file_base = out_path + os.sep + file
            base, _ = os.path.splitext(out_file_base)
            if ext.lower() == '.xlsx':
                out_file_base = base
            out_file = out_file_base + '.bundle'
            if not os.path.exists(out_file) or os.path.isdir(out_file):
                print(f'{out_file} DNE')
            argv_line = [executable_path, '-in', abs_file, out_file]
            print(f'inserting to {out_file}')
            subprocess_list.append(subprocess.Popen(argv_line))


parse_recursively(input_dir, output_dir, engage_xml_path, ignored_exts, subprocess_lst)
print('waiting subprocesses to be done...')
for sp in subprocess_lst:
    sp.wait()
