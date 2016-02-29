author = "Li Pidong"
email = "hope-dream@163.com"
"""
采用indigo将sdf文件转换为png图片
"""
from indigo import *
from indigo_renderer import *
import os
from os.path import isfile, join
indigo = Indigo()
indigoRenderer = IndigoRenderer(indigo)
dir_path = '/Volumes/lpdbxy/work/RFile/weiyao/data/database/sdf_optimize'
sdf_files =  [join(dir_path,file) for file in  os.listdir(dir_path) if isfile(join(dir_path,file)) and file.endswith('.sdf')]

indigo.setOption("smart-layout", "true")
indigo.setOption("render-bond-length", "100")
indigo.setOption("render-output-format", 'png')
# indigo.setOption('render-relative-thickness',2)
# indigo.setOption("render-grid-title-property", "grid-comment")
# indigo.setOption("render-grid-margins", "20, 10")
# indigo.setOption("render-grid-title-offset", "5")
# indigo.setOption("render-image-size", 1300,1300)
indigo.setOption("render-margins", "100, 10")
# indigo.setOption("render-image-width", 1000)
indigo.setOption("render-image-width", "1000")

# indigo.setOption("render-label-mode", 'none')
# indigoRenderer.rendeToFile(array, None, 1, "structures.png")

image_path = './png'
for file in sdf_files:
    try:
        for sdf in indigo.iterateSDFile(file):
            sdf.layout()
            file_id = os.path.splitext(os.path.split(file)[1])[0]
            print(file_id)
            image_name = ''.join([file_id, '.png'])
            indigoRenderer.renderToFile(sdf, join(image_path, image_name))
    except:
        print(file)
        pass




