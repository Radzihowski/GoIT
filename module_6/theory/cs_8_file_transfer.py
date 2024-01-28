# Перенесення файлу

from pathlib import Path

old_dir = Path('data.csv')
new_dir = Path('Temp/test_data.csv')

old_dir.rename(new_dir)