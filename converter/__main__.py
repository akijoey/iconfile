from . import setting
from . import repeat
from . import convert

import os

input_path, output_path = setting.read()
if not os.path.exists(output_path):
	os.mkdir(output_path)
repeat.enum(input_path, output_path, convert.svg2ico)
print('Convert complate')
