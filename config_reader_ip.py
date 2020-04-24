
import configparser
import os

#get the config object from the config parser
def get_config_obj():
    #configuration file path,its give the parent dir
    config_path = os.path.abspath('.\\config.ini')
    if os.path.exists(config_path):
        config = configparser.ConfigParser()
        #Read the content of the file
        config.read(config_path)
    else:
        raise FileNotFoundError(
            'Config file is NOT present as "' + config_path + '" !')
    return config
#get the  data from config.ini key value paire
def get(section, item):
    #get the config object from get_config_obj function
    config=get_config_obj()
    #print the all sections in the file

    try:
        ret = config[section][item]
    except KeyError:
        raise LookupError(f'{item} in section {section} not found in config file') from None
    return ret


