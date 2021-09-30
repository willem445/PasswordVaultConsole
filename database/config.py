import platform

if platform.system() == 'Windows':
    SQLITE_DB_PATH = 'C:\Projects\PasswordVault\PasswordVault.Data\TestDb\PasswordDb.sqlite'
else:
    SQLITE_DB_PATH = 'PasswordDb.sqlite'