from os import path, makedirs, listdir

from init_utils import env_path, env_file, env_file_content

if not path.isdir(env_path):
    makedirs(env_path)

if len(listdir(env_path)) == 0:
    if not path.isfile(env_file):
        with open(path.join(env_path, env_file), 'w') as env_file_to_write:
            env_file_to_write.write(env_file_content)
