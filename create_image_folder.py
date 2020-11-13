import os
import shutil

output_dir = './images'

os.mkdir(output_dir)

for root, dirs, files in os.walk('./my-processed-dataset'):
    print(root)
    print(dirs)
    for filename in files:
        # print(filename)
        if 'jpg' in filename:
            # img_name = root.split('/')[-1].split('_')[0] + '.jpg'
            img_name = root.split('/')[-1].split('_')[0] + filename
            shutil.copy2(os.path.join(root, filename), os.path.join(output_dir, img_name))