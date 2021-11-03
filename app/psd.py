from psd_tools import PSDImage

psd_name = "your_name"
x = 0
psd = PSDImage.open('your_file.psd')

for layer in psd:
    x+=1
    if layer.kind == "smartobject":
        image.conmpose().save(psd_name + str(x) + "png")

# from win32com.client import Dispatch
# import os, sys
# #Save location
# # save_location = 'C:\\Users\\Vadim\\Desktop\\Civil War 1917-1922\\Widowmaker-1917-1922\\app'

# #call photoshop
# psApp = Dispatch('Photoshop.Application')

# psApp.Open(r"C:\\Users\\Vadim\\Desktop\\Civil War 1917-1922\\Widowmaker-1917-1922\\app\\mp.psd")

# options = Dispatch('Photoshop.ExportOptionsSaveForWeb')
# options.Format = 13   # PNG
# options.PNG8 = False  # Sets it to PNG-24 bit

# doc = psApp.activeDocument

# #Hide the layers so that they don't get in the way when exporting
# for layer in doc.layers:
#     layer.Visible = False

# #Now go through one at a time and export each layer
# for layer in doc.layers:

#     #build the filename
#     savefile = save_location + layer.name + '.png'

#     print ('Exporting', savefile)

#     #Set the current layer to be visible        
#     layer.visible = True

#     #Export the layer
#     doc.Export(ExportIn=savefile, ExportAs=2, Options=options)

#     #Set the layer to be invisible to make way for the next one
#     layer.visible = False