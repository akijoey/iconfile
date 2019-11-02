import winreg

ICON_PATH = r'D:\Medium\Picture\Material\Icon\file'
FILE_TYPE = [
	'html',
	'css',
	'js',
	'php',
	'vue',
	'ts',
	'scss',
	'json',
	'xml',
	'sql',
]

def EnumFileType(path):
	for name in FILE_TYPE:
		kpath = '.' + name
		vpath = kpath + r'_auto_file'
		registryUpdate(kpath, vpath)
		kpath = '.' + name + r'_auto_file\Defaulticon'
		vpath = path + r'\file_type_' + name + '.ico'
		registryUpdate(kpath, vpath)
		kpath = '.' + name + r'_auto_file\shell\open\command'
		vpath = r'"D:\Tool\VSCode\Code.exe" "%1"'
		registryUpdate(kpath, vpath)
		print('.' + name + ' successful update')
	print('Please restart system')

def registryUpdate(kpath, vpath):
	with winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, kpath, 0, winreg.KEY_ALL_ACCESS) as key:
		winreg.SetValue(key, '', winreg.REG_SZ, vpath)

if __name__ == '__main__':
	EnumFileType(ICON_PATH)