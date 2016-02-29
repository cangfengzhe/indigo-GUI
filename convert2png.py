from indigo import *
indigo = Indigo()
from indigo_renderer import *
indigoRenderer = IndigoRenderer(indigo)
array = indigo.createArray()
# for mol1 in indigo.iterateSmilesFile(file):
#     mol2 = mol1.clone()
#     indigo.setOption("smart-layout", "false")
#     mol1.layout()
#     mol1.setProperty("grid-comment", "simple")
#     array.arrayAdd(mol1)
#     indigo.setOption("smart-layout", "true")
#     mol2.layout()
#     mol2.setProperty("grid-comment", "smart")
#     array.arrayAdd(mol2)
#
# indigo.setOption("render-bond-length", "14")
# indigo.setOption("render-grid-title-property", "grid-comment")
# indigo.setOption("render-grid-margins", "20, 10")
# indigo.setOption("render-grid-title-offset", "5")
#
# indigoRenderer.renderGridToFile(array, None, 2, 'result.png')



indigo.setOption("standardize-keep-largest", "true")
indigo.setOption("standardize-charges", True);
indigo.setOption("standardize-stereo", True);


arr = indigo.createArray();

for mol in indigo.iterateSDFile("M0019.sdf"):
    indigo.setOption("smart-layout", "true")
    mol.layout()
    array.arrayAdd(mol)

# indigo.setOption("render-bond-length", "154")
indigo.setOption("render-output-format", 'png')
# indigo.setOption('render-relative-thickness',2)
# indigo.setOption("render-grid-title-property", "grid-comment")
# indigo.setOption("render-grid-margins", "20, 10")
# indigo.setOption("render-grid-title-offset", "5")
# indigo.setOption("render-image-size", 300,300)
indigo.setOption("render-margins", 30,30)
indigo.setOption("render-label-mode", 'none')
# indigoRenderer.rendeToFile(array, None, 1, "structures.png")
indigo.setOption("render-image-width", 1000)
indigoRenderer.renderToFile(mol,'structures.png')

#
# indigo.setOption("standardize-charges", True);
#
# mol1 = indigo.loadMolecule("CN(=O)=O")
#
# mol2 = mol1.clone()
#
# mol2.standardize()
#
# array = indigo.createArray()
#
# mol1.setProperty("grid-comment", "before")
# mol2.setProperty("grid-comment", "after")
#
# array.arrayAdd(mol1)
# array.arrayAdd(mol2)
#
# indigo.setOption("render-grid-title-property", "grid-comment")
# indigo.setOption("render-grid-margins", "20, 10")
# indigo.setOption("render-grid-title-offset", "10")
#
# indigoRenderer.renderGridToFile(array, None, 2, 'result.png')
#
