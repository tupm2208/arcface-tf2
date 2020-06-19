import os
import shutil
from glob import glob
from tqdm import tqdm


def count_max_min(path):
    list_ids = os.listdir(path)
    mx = -1
    mn = 10000
    total = 0
    sm = 0

    for idx in tqdm(list_ids):
        no_img = len(os.listdir(os.path.join(path, idx)))
        total += no_img

        if no_img > mx:
            mx = no_img

        if no_img < mn:
            mn = no_img

        if no_img < 100:
            sm += 1

    print(f'max: {mx}\tmin: {mn}')
    print(f'total: {total}')
    print(f'smaller than 30: {sm}')


def move(path, output):
    os.makedirs(output, exist_ok=True)
    list_ids = os.listdir(path)
    total = 0
    cr_list = os.listdir(output)

    for idx in tqdm(list_ids):
        if idx in cr_list:
            continue
        f_path = os.path.join(path, idx)
        image_list = [os.path.join(f_path, e) for e in os.listdir(f_path)[:50]]
        no_img = len(image_list)
        if no_img < 30:
            continue
        total += no_img
        for src in image_list:
            splited = src.split('/')
            des = os.path.join(output, splited[-2], splited[-1])
            os.makedirs('/'.join(des.split('/')[:-1]), exist_ok=True)
            # print('/'.join(des.split('/')[:-1]))
            shutil.copy(src, des)



if __name__ == '__main__':
    count_max_min('/home/tupm/datasets/train')
    # move('/home/tupm/SSD/datasets/face_data/ms1m_align_112/imgs', '/home/tupm/datasets/train')