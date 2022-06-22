from codecs import lookup_error
import os
import shutil

if __name__ == '__main__':
    store_path = '/home/ubuntu/kartik/STEGO/datasets/cocostuff/curated/test2017/Coco164kFull_Stuff_Coarse.txt'
    imgs_dir = '/home/ubuntu/kartik/STEGO/datasets/cocostuff/images/test2017'
    anno_dir = '/home/ubuntu/kartik/STEGO/datasets/cocostuff/annotations/test2017'
    lookup_path = '/home/ubuntu/kartik/STEGO/datasets/cocostuff/annotations/val2017'
    
    files = []
    
    for img_path in os.listdir(imgs_dir):
        
        src_path = os.path.join(lookup_path, img_path.replace('.jpg', '.png'))
        dest_path = os.path.join(anno_dir, img_path.replace('.jpg', '.png'))

        shutil.copy(src_path, dest_path)
        
        files.append(img_path.replace('.jpg', ""))
        
    with open(store_path, 'w') as sp:
        for f_path in files:
            sp.write(f_path)
            sp.write('\n')
                