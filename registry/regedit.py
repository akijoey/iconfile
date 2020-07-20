import winreg

def update(key, value):
	with winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, key, 0, winreg.KEY_ALL_ACCESS) as ex:
		winreg.SetValue(ex, '', winreg.REG_SZ, value)
