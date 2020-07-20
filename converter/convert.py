from wand.image import Image

def svg2ico(input_path, output_path, file_name):

	# get file name and file suffix
	index = file_name.index('.')
	name = file_name[:index]
	suffix = file_name[index:]
	if suffix != '.svg':
		return

	# get input file and output file
	input_file = input_path + file_name
	output_file = output_path + name + '.ico'

	# convert input file and save to output file
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
