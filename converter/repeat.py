import os

def enum(input_path, output_path, callback):

	# function exit
	if not os.path.isdir(input_path):
		print('Error: "', input_path, '" is not a directory or does not exist.')
		return

	# exec callback recursively
	list_dirs = os.walk(input_path)
	for root, dirs, files in list_dirs:
		for d in dirs:
			enum(os.path.join(root, d), output_path, callback)
		for f in files:
			callback(root, output_path, f)
