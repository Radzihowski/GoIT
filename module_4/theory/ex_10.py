import shutil

print(shutil.get_archive_formats())

archive_file = shutil.make_archive('my_archive_name', 'zip', 'temp')
print(archive_file)
shutil.unpack_archive(archive_file, 'Hello')