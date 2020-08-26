import sys
import os
import cv2

def main(argv):
    for f in argv:
        #fn = os.path.split(f)[1].split('.')[0]
        fname = "crop-" + f
        img = cv2.imread(f)
        crop_img = img[0:1000,0:1920]
        cv2.imwrite(fname,crop_img)

if __name__ == "__main__":
    main(sys.argv[1:])


    
