import os
from configparser import ConfigParser

def read():

	# get config path
	root_path = os.getcwd() + '\\'
	config_path = root_path + 'config.ini'

	# read config
	config = ConfigParser()
	config.read(config_path, encoding = 'utf-8')

	# get absolute icon path and vscode path
	icon_path = root_path + config.get('Relative', 'output')
	vscode_path = config.get('Absolute', 'vscode')
	return icon_path, vscode_path
