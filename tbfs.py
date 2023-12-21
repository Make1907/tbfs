#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
# from datetime import date
import datetime

from skimage import exposure
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2


def cal_hist_gray_bar(path, save_path):
    for filename in os.listdir(path):
        print(filename)
        img = cv2.imread(path + os.sep + filename, 0)
        # 画出每张图的灰度直方图
        plt.figure()
        plt.hist(img.ravel(), 256, density=1,)
        font = 20
        plt.ylabel('Density', fontsize=font)
        plt.xlabel('Gray Value', fontsize=font)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        # plt.hist(img.ravel(), 256, density=1, histtype='bar', alpha=0.75, rwidth=0.8)
        # plt.show()
        plt.ylim(0, 0.06)
        plt.savefig(save_path + os.sep + filename, dpi=150, bbox_inches='tight')
        plt.close()


def int_sub(path, save_path):
    os.chdir(path)
    img0 = cv2.imread('\\dir_of_image.tif', 0)  # 注意图片格式
    img1 = cv2.imread('\\dir_of_image.tif', 0)  # 注意图片格式
    # print(img0.shape)
    # filename = path + os.sep + "147.tif"
    for filename in os.listdir():
        img = cv2.imread(filename, 0)
        n = 30
        print(filename)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if int(img[i][j]) - int(img0[i][j]) >= 10:
                    img[i][j] = img[abs(i - n)][j]
                    # pass
                elif int(img[i][j]) - int(img0[i][j]) <= -15:
                    img[i][j] = img[abs(i - n)][j]
                else:
                    img[i][j] = (int(img[i][j]) - int(img0[i][j]) + 20)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img1[i][j] == 0:
                    img[i][j] = img[abs(i - n)][j]
        # img = img * 5
        cv2.imwrite(save_path + os.sep + filename, img)


def int_sub_dissolve_few_grain_single(path, save_path):
    os.chdir(path)
    img0 = cv2.imread('\\dir_of_image.tif', 0)  # 注意图片格式
    img1 = cv2.imread('\\dir_of_image.tif', 0)  # 注意图片格式
    # print(img0.shape)
    filename = path + os.sep + "147.tif"
    img = cv2.imread(filename, 0)
    count = 0
    n = 30
    print(filename)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if int(img[i][j]) - int(img0[i][j]) >= 2:
                img[i][j] = img[abs(i - n)][j]

            elif int(img[i][j]) - int(img0[i][j]) <= -15:
                img[i][j] = img[abs(i - n)][j]
            else:
                img[i][j] = (int(img[i][j]) - int(img0[i][j]) + 20)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img1[i][j] == 0:
                img[i][j] = img[abs(i - n)][j]

            if img[i][j] >= 30:
                count = count + 1
    img = img * 5
    print(count)
    cv2.imwrite(save_path + os.sep + "147_20200103.tif", img)


def int_sub_more_grain(path, save_path):
    os.chdir(path)
    img0 = cv2.imread('\\dir_of_image.tif', 0)  # 注意图片格式
    # img1 = cv2.imread('D:\\Program data\\xujin\\xujin_make\\ps_diban\\diban_white.tif', 0)  # 注意图片格式
    # print(img0.shape)
    # filename = path + os.sep + "147.tif"
    for filename in os.listdir():
        img = cv2.imread(filename, 0)
        n = 30
        print(filename)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                # cv2.imwrite(save_path + os.sep + "025_%d.tif" % n, img)
                if int(img[i][j]) - int(img0[i][j]) >= 5:
                    img[i][j] = 15
                elif int(img[i][j]) - int(img0[i][j]) <= -5:
                    img[i][j] = 1
                # decrease the value if value<=o
                # elif int(img[i][j]) - int(img0[i][j]) < 0 and int(img[i][j]) - int(img0[i][j]) > -5:
                #     img[i][j] = int(img[i][j]) - int(img0[i][j]) + 5
                # elif int(img[i][j]) - int(img0[i][j]) >= 0 and int(img[i][j]) - int(img0[i][j]) <= 5:
                #     img[i][j] = int(img[i][j]) - int(img0[i][j]) + 10
                # add a num for all value
                else:
                    img[i][j] = (int(img[i][j]) - int(img0[i][j]) + 10)
        cv2.imwrite(save_path + os.sep + filename, img)
        img = img * 10
        cv2.imwrite(save_path + os.sep + 'mutil_10' + os.sep + filename, img)


def int_sub_less_grain(path, save_path):
    os.chdir(path)
    img0 = cv2.imread('dir_of_image\\105.tif', 0)  # 注意图片格式
    img1 = cv2.imread('\\dir_of_image.tif', 0)  # 注意图片格式
    # print(img0.shape)
    # filename = path + os.sep + "147.tif"
    for filename in os.listdir():
        img = cv2.imread(filename, 0)
        n = 30
        print(filename)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if int(img[i][j]) - int(img0[i][j]) >= 5:
                    img[i][j] = 15
                elif int(img[i][j]) - int(img0[i][j]) <= -5:
                    img[i][j] = 3
                elif int(img[i][j]) - int(img0[i][j]) < 0 and int(img[i][j]) - int(img0[i][j]) > -5:
                    img[i][j] = int(img[i][j]) - int(img0[i][j]) + 5
                elif int(img[i][j]) - int(img0[i][j]) >= 0 and int(img[i][j]) - int(img0[i][j]) < 5:
                    img[i][j] = int(img[i][j]) - int(img0[i][j]) + 10
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img1[i][j] == 0:
                    img[i][j] = img[abs(i - n)][j]
        cv2.imwrite(save_path + os.sep + filename, img)
        # img = img * 8
        # cv2.imwrite(save_path + os.sep + 'contrast' + filename, img)


def sub_more_grain_single(path, save_path):
    os.chdir(path)
    img0 = cv2.imread('\\dir_of_image', 0)  # 注意图片格式
    # img1 = cv2.imread('D:\\Program data\\xujin\\xujin_make\\ps_diban\\diban_white.tif', 0)  # 注意图片格式
    # print(img0.shape)
    filename = path + os.sep + "025.tif"
    img = cv2.imread(filename, 0)
    count2 = 0
    n = 3
    num = []
    x = range(-20, 20)
    print(filename)
    # for n in x:
    img_res = img.copy()
    count1 = 0
    # cv2.imwrite(save_path + os.sep + "025_%d.tif" % n, img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # cv2.imwrite(save_path + os.sep + "025_%d.tif" % n, img)
            if int(img[i][j]) - int(img0[i][j]) >= 5:
                img_res[i][j] = 15
            elif int(img[i][j]) - int(img0[i][j]) <= -5:
                img_res[i][j] = 1
            elif int(img[i][j]) - int(img0[i][j]) < 0 and int(img[i][j]) - int(img0[i][j]) > -5:
                img_res[i][j] = int(img[i][j]) - int(img0[i][j]) + 5
            elif int(img[i][j]) - int(img0[i][j]) >= 0 and int(img[i][j]) - int(img0[i][j]) <= 5:
                img_res[i][j] = int(img[i][j]) - int(img0[i][j]) + 10
            # else:
            #     img_res[i][j] = (int(img[i][j]) - int(img0[i][j]) + 10)
    num.append(count1)
    print(n)
    img_res = img_res * 14
    cv2.imwrite(save_path + os.sep + "025_%d.tif" % n, img_res)
    print(num)
    # plt.figure()
    # plt.bar(x, num)
    # plt.show()
    # for i in range(img.shape[0]):
    #     for j in range(img.shape[1]):
    #         if img1[i][j] == 0:
    #             img[i][j] = img[abs(i - n)][j]
    #
    #         if img[i][j] >= 30:
    #             count = count + 1
    # img = img * 5


def contrast(path, save_path):
    os.chdir(path)
    for filename in os.listdir():
        print(filename)
        img = cv2.imread(filename, 0)
        img = img * 8 + 20
        cv2.imwrite(save_path + os.sep + filename, img)


# int_sub('D:\\Program data\\xujin\\xujin_make\\20200102_denoise\\ori_105_begain',
#         'D:\\Program data\\xujin\\xujin_make\\20200102_denoise\\final_result003_ori')
# contrast('D:\\Program data\\xujin\\xujin_make\\20200102_denoise\\final_result003_ori',
#          'D:\\Program data\\xujin\\xujin_make\\20200102_denoise\\final_result003_cheng7_50')
# contrast('D:\\Program data\\xujin\\more_grain\\result001',
#          'D:\\Program data\\xujin\\more_grain\\result001_cheng7_50')

# int_sub('D:\\Program data\\xujin\\xujin_make\\20200102_denoise\\ori_105_begain',
#         'D:\\Program data\\xujin\\xujin_make\\20200102_denoise\\final_result_ori')

# int_sub_dissolve_few_grain_single('D:\\Program data\\xujin\\xujin_make\\20200102_denoise\\ori_105_begain',
#                                   'D:\\Program data\\xujin\\xujin_make\\20200102_denoise\\test')
# cal_hist_gray_bar('D:\\Program data\\xujin\\xujin_make\\grad\\mean_blurred_result\\126.tif',
#                   "D:\\Program data\\Mg-RE\\technology_model\\model_result")

# int_sub_more_grain('D:\\Program data\\xujin\\more_grain\\ori',
#                    'D:\\Program data\\xujin\\more_grain\\result_zhijiejia10')

# sub_more_grain_single('D:\\Program data\\xujin\\more_grain\\ori',
#                       'D:\\Program data\\xujin\\more_grain\\single_test')