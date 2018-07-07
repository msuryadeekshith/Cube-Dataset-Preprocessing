import cv2
import numpy as np
import scipy.misc
import sys

def apply_changes(i=1, mask=1, save=1):

    file_path = 'data/Cube/images/' + str(i)+'.png'

    print('processing: '+str(i)+'.png ...')
    img = np.array(cv2.imread(file_path, -1), dtype='float32')

    saturation_level = np.amax(img)-2
    black_level = 2048
    img = img - black_level
    img.clip(0)

    m = np.zeros((img.shape[0], img.shape[1]))
    for ch in range(0,3):
        m = np.logical_or(m, img[:,:,ch] >= (saturation_level - black_level))

    if(mask!=0):
        m[1050:m.shape[0], 2050:m.shape[1]]

    m = np.dstack((m,m,m))
    img[m==True] = 0

    img1 = img[...,[2,1,0]]

    if(save==1):
        file_path_op = 'data/Cube/images/' + str(i)+'_p.png'
        scipy.misc.toimage(img1,cmin=0.0).save(file_path_op)
        print('done: ' + file_path_op)


if __name__ == '__main__':

    if(len(sys.argv)==1):
        apply_changes()
    elif(len(sys.argv)==2):
        apply_changes(sys.argv[1])
    elif(len(sys.argv)==3):
        for i in range(int(sys.argv[1]), int(sys.argv[2])+1):
            apply_changes(i)
