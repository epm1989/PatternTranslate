
class Setting:
    specification = r'%\{\d[GS\d]{,2}\}' or r'\%\{[A-Za-z\d]{1,3}\}'
    capture_group = '(.+)'
