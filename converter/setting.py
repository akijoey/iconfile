import os
from configparser import ConfigParser

def read():

	# get config path
	root_path = os.getcwd() + '\\'
	config_path = root_path + 'config.ini'

	# read config
	config = ConfigParser()
	config.read(config_path, encoding = 'utf-8')

	# get absolute input path and output path
	input_path = root_path + config.get('Relative', 'input')
	output_path = root_path + config.get('Relative', 'output')
	return input_path, output_path
