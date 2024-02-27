# -*- coding: utf-8 -*-

import os
root = '/Users/alikanafin/Desktop/em_video'

#annotation_file = 'annotations_croppad_fold'+str(fold+1)+'.txt'
annotation_file = 'annotations.txt'

for video in os.listdir(root):
    if not video.endswith('.npy') or 'croppad' not in video:
        continue
    
    audio = video.split('_face')[0] + '_croppad.wav'  
    # print(str(audio))
    with open(annotation_file, 'a') as f:
        f.write(os.path.join(root, video) + ';' + os.path.join(root, audio) + ';'+ str(1) + ';testing' + '\n')





