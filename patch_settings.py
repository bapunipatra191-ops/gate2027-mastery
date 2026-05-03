import os

filepath = r'c:\Users\bapun\OneDrive\Desktop\army1\gate_project\settings.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add imports if not present
if 'import dj_database_url' not in content:
    content = content.replace('from pathlib import Path', 'from pathlib import Path\nimport os\nimport dj_database_url')

# Add database url config if not present
if 'dj_database_url.config' not in content:
    old_db = """DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""
    new_db = """DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
if db_from_env:
    DATABASES['default'].update(db_from_env)
"""
    content = content.replace(old_db, new_db)
    
    # Handle the case where line endings are \r\n
    old_db_crlf = old_db.replace('\n', '\r\n')
    new_db_crlf = new_db.replace('\n', '\r\n')
    content = content.replace(old_db_crlf, new_db_crlf)

with open(filepath, 'w', encoding='utf-8', newline='') as f:
    f.write(content)
