from cx_Freeze import setup, Executable

APP_NAME = "Cabal JTool"
APP_VERSION = "v5.70"
APP_DESCRIPTION = "A Cabal Online Macro and Automation."

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': [], 'includes': ['pynput.keyboard._win32', 'pynput.mouse._win32'], 'include_files': ['instructions.txt', 'setup/', 'data/', 'img/', 'LICENSE', 'jtool.ico']}

base = 'gui'

executables = [
    Executable('jtool.pyw', base=base)
]

setup(name=APP_NAME,
      version = APP_VERSION,
      description = APP_DESCRIPTION,
      options = {'build_exe': build_options},
      executables = executables)
