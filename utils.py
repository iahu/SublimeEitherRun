import os
import platform

def is_windows():
    return platform.system() == 'Windows' or os.name == 'nt'

def env_path_contains(path_to_look_for, env_path=None):
    """Check if the specified path is listed in OS environment path.

    :param path_to_look_for: The path the search for.
    :param env_path: The environment path str.
    :return: True if the find_path exists in the env_path.
    :rtype: bool
    """
    if not path_to_look_for:
        return False
    if not env_path:
        env_path = os.environ['PATH']
    path_to_look_for = str.replace(path_to_look_for, os.pathsep, '')
    paths = env_path.split(os.pathsep)
    for path in paths:
        if path == path_to_look_for:
            return True
    return False

def get_proc_env():
    env = None
    if not is_windows():
        env = os.environ.copy()
        usr_path = ':/usr/local/bin'
        if not env_path_contains(usr_path) and env_path_exists(usr_path):
            env['PATH'] += usr_path
    return env
