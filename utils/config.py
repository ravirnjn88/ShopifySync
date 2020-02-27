"""Get configs from secret file."""
import os
import configparser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = configparser.ConfigParser(allow_no_value=True)
config.read(BASE_DIR + '/etc/config/secrets.ini')


def get(section, key):
    """getter function to get values from config directly."""

    return config[section][key]