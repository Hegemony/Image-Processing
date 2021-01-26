from PIL import Image
import os, glob


def batch_image(in_dir, out_dir):
    if not os.path.exists(out_dir):
        print(out_dir, 'is not existed.')
        os.mkdir(out_dir)

    if not os.path.exists(in_dir):
        print(in_dir, 'is not existed.')
        return -1
    count = 0
    for files in glob.glob(in_dir + '/*'):
        filepath, filename = os.path.split(files)

        # out_file = filename[0:9] + '.jpg'
        out_file = filename[8:12] + '.jpg'
        # print(filepath,',',filename, ',', filename[9:13],'.', out_file)
        im = Image.open(files)
        new_path = os.path.join(out_dir, out_file)
        print(count, ',', new_path)
        count = count + 1
        im.save(os.path.join(out_dir, out_file))


if __name__ == '__main__':
    in_dir = '/home/notebook/data/group//branch/SR/SISR/text_dataset/ICDAR2015-TextSR/DATA/TEST/HD/'
    out_dir = './IC15-SR/TEST/HD/'
    batch_image(in_dir, out_dir)