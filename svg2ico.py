import os
from wand.image import Image

INPUT_PATH = r'C:\Users\10106\Desktop\svg'
OUTPUT_PATH = r'C:\Users\10106\Desktop\ico'

def EnumPathFiles(path, callback):
	if not os.path.isdir(path):
		print('Error: "', path, '" is not a directory or does not exist.')
		return
	list_dirs = os.walk(path)
	for root, dirs, files in list_dirs:
		for d in dirs:
			EnumPathFiles(os.path.join(root, d), callback)
		for f in files:
			callback(root, f)

def svg2ico(path, filename):
	filename = str(filename)
	i = filename.index('.')
	fname = filename[:i]
	fext = filename[i:]
	if fext !='.svg':
		return
	input_file = str(path + '\\' + filename)
	output_file = OUTPUT_PATH + '\\' + fname + '.ico'
	with Image(width = 128, height = 128, filename = input_file, background = 'transparent') as ico:
		with Image(width = 64, height = 64, filename = input_file, background = 'transparent') as sico:
			ico.sequence.append(sico)
		with Image(width = 48, height = 48, filename = input_file, background = 'transparent') as sico:
			ico.sequence.append(sico)
		with Image(width = 32, height = 32, filename = input_file, background = 'transparent') as sico:
			ico.sequence.append(sico)
		with Image(width = 16, height = 16, filename = input_file, background = 'transparent') as sico:
			ico.sequence.append(sico)
		ico.save(filename = output_file)
	print(output_file)

if __name__ == '__main__':
	EnumPathFiles(INPUT_PATH, svg2ico)