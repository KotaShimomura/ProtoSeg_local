#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Donny You(youansheng@gmail.com)
# CityScape Seg data generator.


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import argparse
import shutil


IMAGE_DIR = 'image'
LABEL_DIR = 'label'

def str2bool(v):
    """ Usage:
    parser.add_argument('--pretrained', type=str2bool, nargs='?', const=True,
                        dest='pretrained', help='Whether to use pretrained models.')
    """
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Unsupported value encountered.')


class CityscapesGenerator(object):

    def __init__(self, args, image_dir=IMAGE_DIR, label_dir=LABEL_DIR):
        self.args = args
        self.train_label_dir = os.path.join(self.args.save_dir, 'train', label_dir)
        self.val_label_dir = os.path.join(self.args.save_dir, 'val', label_dir)
        self.coarse_label_dir = os.path.join(self.args.save_dir, 'coarse', label_dir)
        if not os.path.exists(self.train_label_dir):
            os.makedirs(self.train_label_dir)

        if not os.path.exists(self.val_label_dir):
            os.makedirs(self.val_label_dir)

        if not os.path.exists(self.coarse_label_dir):
            os.makedirs(self.coarse_label_dir)

        self.train_image_dir = os.path.join(self.args.save_dir, 'train', image_dir)
        self.val_image_dir = os.path.join(self.args.save_dir, 'val', image_dir)
        self.coarse_image_dir = os.path.join(self.args.save_dir, 'coarse', image_dir)

        if not os.path.exists(self.train_image_dir):
            os.makedirs(self.train_image_dir)

        if not os.path.exists(self.val_image_dir):
            os.makedirs(self.val_image_dir)

        if not os.path.exists(self.coarse_image_dir):
            os.makedirs(self.coarse_image_dir)

    def generate_label(self):
        if not self.args.coarse:
            ori_train_img_dir = os.path.join(self.args.ori_root_dir, 'leftImg8bit/train')
            ori_train_label_dir = os.path.join(self.args.ori_root_dir, 'gtFine/train')
            ori_val_img_dir = os.path.join(self.args.ori_root_dir, 'leftImg8bit/val')
            ori_val_label_dir = os.path.join(self.args.ori_root_dir, 'gtFine/val')
            
            print("dir config")

            for image_file in self.__list_dir(ori_train_img_dir):
                image_name = '_'.join(image_file.split('_')[:-1])
                label_file = '{}_gtFine_labelIds.png'.format(image_name)
                shotname, extension = os.path.splitext(image_file.split('/')[-1])
                shutil.copy(os.path.join(ori_train_img_dir, image_file),
                            os.path.join(self.train_image_dir, '{}{}'.format(shotname, extension)))
                shutil.copy(os.path.join(ori_train_label_dir, label_file),
                            os.path.join(self.train_label_dir, '{}.png'.format(shotname)))
            print("pass1")

            for image_file in self.__list_dir(ori_val_img_dir):
                image_name = '_'.join(image_file.split('_')[:-1])
                label_file = '{}_gtFine_labelIds.png'.format(image_name)
                shotname, extension = os.path.splitext(image_file.split('/')[-1])
                shutil.copy(os.path.join(ori_val_img_dir, image_file),
                            os.path.join(self.val_image_dir, '{}{}'.format(shotname, extension)))
                shutil.copy(os.path.join(ori_val_label_dir, label_file),
                            os.path.join(self.val_label_dir, '{}.png'.format(shotname)))
            print("pass2")
            
        else:
            print("else")
            print(self.args.ori_root_dir)
            ori_train_img_dir = os.path.join(self.args.ori_root_dir, 'leftImg8bit/train')
            ori_train_label_dir = os.path.join(self.args.ori_root_dir, 'gtCoarse/train')
            ori_train_extra_img_dir = os.path.join(self.args.ori_root_dir, 'leftImg8bit/train_extra')
            ori_train_extra_label_dir = os.path.join(self.args.ori_root_dir, 'gtCoarse/train_extra')
            ori_val_img_dir = os.path.join(self.args.ori_root_dir, 'leftImg8bit/val')
            ori_val_label_dir = os.path.join(self.args.ori_root_dir, 'gtCoarse/val')
            
            print("dir config")

            for image_file in self.__list_dir(ori_train_img_dir):
                image_name = '_'.join(image_file.split('_')[:-1])
                label_file = '{}_gtCoarse_labelIds.png'.format(image_name)
                print(image_name)
                print(label_file)
                
                shotname, extension = os.path.splitext(image_file.split('/')[-1])
                
                print("end shot ext")
                shutil.copy(os.path.join(ori_train_img_dir, image_file),
                            os.path.join(self.train_image_dir, '{}{}'.format(shotname, extension)))
                print("pass copy 1")
                
                print(ori_train_label_dir)
                print(label_file)
                print(self.train_label_dir)
                print(shotname)
                shutil.copy(os.path.join(ori_train_label_dir, label_file),
                            os.path.join(self.train_label_dir, '{}.png'.format(shotname)))
                #/tmp/working/workspace/ProtoSeg_local/data/original_cityscapes/gtCoarse/train + jena/jena_000084_000019_gtCoarse_labelIds.png
                print("pass copy 2")
                
            print("pass for1")

            for image_file in self.__list_dir(ori_train_extra_img_dir):
                image_name = '_'.join(image_file.split('_')[:-1])
                label_file = '{}_gtCoarse_labelIds.png'.format(image_name)
                shotname, extension = os.path.splitext(image_file.split('/')[-1])
                shutil.copy(os.path.join(ori_train_extra_img_dir, image_file),
                            os.path.join(self.coarse_image_dir, '{}{}'.format(shotname, extension)))
                shutil.copy(os.path.join(ori_train_extra_label_dir, label_file),
                            os.path.join(self.coarse_label_dir, '{}.png'.format(shotname)))
                
            print("pass for2")

            for image_file in self.__list_dir(ori_val_img_dir):
                image_name = '_'.join(image_file.split('_')[:-1])
                label_file = '{}_gtCoarse_labelIds.png'.format(image_name)
                shotname, extension = os.path.splitext(image_file.split('/')[-1])
                shutil.copy(os.path.join(ori_val_img_dir, image_file),
                            os.path.join(self.val_image_dir, '{}{}'.format(shotname, extension)))
                shutil.copy(os.path.join(ori_val_label_dir, label_file),
                            os.path.join(self.val_label_dir, '{}.png'.format(shotname)))
            print("pass for3")


    def __list_dir(self, dir_name):
        filename_list = list()
        for item in os.listdir(dir_name):
            if os.path.isdir(os.path.join(dir_name, item)):
                for filename in os.listdir(os.path.join(dir_name, item)):
                    filename_list.append('{}/{}'.format(item, filename))
            else:
                filename_list.append(item)
                
                
        print("pass listdir")
        return filename_list


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--coarse', type=str2bool, nargs='?', default=False,
                        dest='coarse', help='Whether is the coarse data.')
    parser.add_argument('--save_dir', default=None, type=str,
                        dest='save_dir', help='The directory to save the data.')
    parser.add_argument('--ori_root_dir', default=None, type=str,
                        dest='ori_root_dir', help='The directory of the cityscapes data.')

    args = parser.parse_args()

    cityscapes_generator = CityscapesGenerator(args)
    cityscapes_generator.generate_label()

# /root/miniconda3/bin/python cityscapes_generator.py --coarse True \
# --save_dir /msravcshare/dataset/cityscapes/ --ori_root_dir \
# /msravcshare/yuyua/code/segmentation/deeplab_v3/dataset/cityscapes/
