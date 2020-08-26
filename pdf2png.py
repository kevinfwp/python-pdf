import fitz
import sys
import os

def main(argv):
    for f in argv:
        doc = fitz.open(f)
        fn = os.path.split(f)[1].split('.')[0]
        for pg in range(doc.pageCount):
            page = doc[pg]
            zoom = int(200)
            rotate = int(0)
            trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
        
            pm = page.getPixmap(matrix=trans, alpha=False)
            fname = fn + "-" + str(pg).zfill(4) + ".png"
            pm.writePNG(fname) 

if __name__ == "__main__":
    main(sys.argv[1:])


    
