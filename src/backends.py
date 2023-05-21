import configparser
from enum import Enum

import panic

GLOBAL_CONFIG_PATH = "../../global.conf"
DEFAULT_HOST = 'localhost'

LARAVEL = 'laravel'
RAILS = 'rails'
ROCKET = 'rocket'
FLASK = 'flask'

def read_conf_value(file_path, section, option):
    config = configparser.ConfigParser()
    config.read(file_path)

    if section in config and option in config[section]:
        return config[section][option]
    else:
        return None

def write_conf_value(file_path, section, option, value):
    config = configparser.ConfigParser()
    config.read(file_path)

    if section not in config:
        config.add_section(section)
    
    config[section][option] = value

    with open(file_path, 'w') as config_file:
        config.write(config_file)

def get_host_name(backend_type):
    # use the enum variant as the section name
    host = read_conf_value(GLOBAL_CONFIG_PATH, backend_type, 'host_name')
    if host is None:
        # fallback on the localhost as a default.
        return DEFAULT_HOST
    return host

def get_port(backend_type):
    port = read_conf_value(GLOBAL_CONFIG_PATH, backend_type, 'port')
    if port is None:
        panic.panic("No port specified for backend " + backend_type)
    return port

def get_endpoint(backend_type):
    return get_host_name(backend_type) + ":" + get_port(backend_type)

def mk_route(backend_type, route):
    return f"http://{get_endpoint(backend_type)}/{route}"
