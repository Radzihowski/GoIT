from pathlib import Path
new_dir = Path('ABC/tempo/TMPS/Exist')
print(new_dir)
new_dir.mkdir(parents=True, exist_ok=True)