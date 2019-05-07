from PIL import Image
import pytesseract
import glob
import time
from io import BytesIO


def convertToJpeg(im):
    with BytesIO() as f:
        im.save(f, format='JPEG')
        f.seek(0)
        ima_jpg = Image.open(f)
    return ima_jpg


start_time = time.time()
f_name = '42555'
fnames = glob.glob('./' + f_name + '/*.jpg')

for filename in fnames:
    im = Image.open(filename)
    # im = ima_jpg
    # im = convertToJpeg(im)
    fn = filename[8:]
    # print(fn[:-4])
    # kdcvn
    text = pytesseract.image_to_string(im, lang='fas')

    with open(fn[:-4] + '.txt', "w", encoding='utf-8') as text_file:
        text_file.write(text)
    print(fn)

print("--- %s seconds ---" % (time.time() - start_time))
print("--- num of files : %s ---" % (len(fnames)))
print("file_name:" + f_name)
