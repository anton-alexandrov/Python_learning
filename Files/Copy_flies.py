import os
import time

source = './Test_Files'
target_dir = 'Test_Files_copy'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr {0} {1}".format(target, ''.join(source))
print(zip_command)
if os.system(zip_command) == 0:
    print('Copy has been created successfully in ', target)
else:
    print('There was an error')
