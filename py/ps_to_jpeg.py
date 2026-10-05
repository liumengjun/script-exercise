"""
把`*.ps(postscript)`文件转换为`jpg`图片
底层使用`gs(ghostscript)`命令, 需要安装`ghostscript`(注意正确安装, 软连接也正常)。
"""
import os
import sys
import glob
from PIL import Image


def ps_to_jpeg_n(ps_pattern: str, overwrite=False):
    count = 0
    skips = 0
    for ps_file in glob.glob(ps_pattern):
        ok = ps_to_jpeg_1(ps_file, overwrite)
        if ok:
            count += 1
        else:
            skips += 1
    return count, skips


def ps_to_jpeg_1(ps_file: str, overwrite=False):
    if (ps_file[-3:].lower() != '.ps') or (not os.path.exists(ps_file)):
        print("no ps file: '%s'" % ps_file)
        return False

    jpg_file = ps_file[:-3] + ".jpg"
    if (not overwrite) and os.path.exists(jpg_file):
        print("jpg exists, skip: '%s'" % jpg_file)
        return False

    img = Image.open(ps_file)
    img.load(scale=2)  # dpi = 72.0 * scale
    img.save(jpg_file, "JPEG", quality=100)
    img.close()
    # os.system("gs -sDEVICE=png16m -r300 -o '%s' '%s'" % (jpg_file, ps_file))
    # os.system("gs -sDEVICE=jpeg -r300 -o '%s' '%s'" % (jpg_file, ps_file))
    print("got jpg: '%s'" % jpg_file)
    return True


if __name__ == "__main__":
    # ps_to_jpeg_1('var/k_1-[r2.3_s1.0]-unit_30px.ps')
    # ps_to_jpeg_n('math_demos/var/*.ps')

    print(sys.argv)
    if len(sys.argv) < 2:
        print("nothing todo, usage: [-f] file1 [file2] ['file*.ps']")
        exit()

    overwrite = sys.argv[1] == '-f' or sys.argv[1] == '--force'
    i_start = overwrite and 2 or 1

    total_count = 0
    total_skips = 0
    for arg in sys.argv[i_start:]:
        print("processing: '%s' ..." % arg)
        if os.path.exists(arg):
            ok = ps_to_jpeg_1(arg, overwrite)
            total_count += ok and 1 or 0
            total_skips += (not ok) and 1 or 0
        else:
            _c, _s = ps_to_jpeg_n(arg, overwrite)
            total_count += _c
            total_skips += _s
    print('total_count: %d, total_skips: %d' % (total_count, total_skips))
    print('end')
