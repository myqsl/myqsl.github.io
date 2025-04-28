import os
from os.path import join, getsize
from subprocess import run

for root, dirs, files in os.walk('assets/qsl'):
    for name in files:
        path = join(root, name)
        size = getsize(path)
        # if 'small' in path and path.endswith('.jpg') and size > 100 * 1000:
        #     print('Not optimized small file: ', path, ' :', size)
        #     # run(f'jpegoptim -m50 {path}', check=True, shell=True)
        
        if 'full' in path and path.endswith('.jpg') and size > 1000 * 1000:
            # run(f'convert -resize 1200 {path} {path}', check=True, shell=True)
            print('Not optimized full file: ', path, ' :', size)
