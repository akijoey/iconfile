import os

def enum(icon_path, vscode_path, callback):

	# function exit
	if not os.path.isdir(icon_path):
		print('Error: "', icon_path, '" is not a directory or does not exist.')
		return

	# exec callback recursively
	list_dirs = os.walk(icon_path)
	for root, dirs, files in list_dirs:
		for d in dirs:
			enum(os.path.join(root, d), vscode_path, callback)
		for f in files:
			name = f[:f.index('.')]
			suffix = '.' + name
			callback(suffix, suffix + r'_auto_file')
			callback(suffix + r'_auto_file\Defaulticon', root + f)
			callback(suffix + r'_auto_file\shell\open\command', '"' + vscode_path + '" "%1"')
			print(suffix + ' successful update')
