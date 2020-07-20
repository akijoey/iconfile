from . import setting
from . import repeat
from . import regedit

import os

icon_path, vscode_path = setting.read()
repeat.enum(icon_path, vscode_path, regedit.update)
print('Please restart system')