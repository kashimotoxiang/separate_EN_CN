from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('separate_EN_CN.py', base=base, targetName = 'separate_EN_CN')
]

setup(name='separate_EN_CN',
      version = '1.0',
      description = 'separate Chinese from Engligh, and insert separation char between them',
      options = dict(build_exe = buildOptions),
      executables = executables)
