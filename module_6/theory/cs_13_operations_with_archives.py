# Робота з архівами. Заархівувати вміст папки та розархівувати

import shutil

archive = shutil.make_archive('backup', 'zip', '../Temp/')
print(archive)
shutil.unpack_archive(archive, '../New_folder')