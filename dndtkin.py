from imageai.Prediction import ImagePrediction
import os
import tkinter as tk
from tkinter import * 
from TkinterDnD2 import DND_FILES, TkinterDnD

file_path = ""
file_name = ""
output = []
inc = 1
def imapre(file_n):
    execution_path=file_n[0]
    prediction= ImagePrediction()

    # prediction.setModelTypeAsSqueezeNet()
    # prediction.setModelPath(os.path.join(execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
    global inc
    prediction.setModelTypeAsResNet()
    prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
    prediction.loadModel()
    predictions, probabilities = prediction.predictImage(os.path.join(execution_path,file_n[1]), result_count=5 )
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        output.append("{} : {}".format(eachPrediction , eachProbability))
        print(output)
    drop_in_list_box(output,inc)
    inc += 1
        
def drop_inside_list_box(event):
    #listb.insert("end", event.data)
    file_path = str(event.data)
    print(file_path)
    file_name = os.path.split(file_path)
    print(file_name[0])
    print(file_name[1])
    listb.insert("end", "{}] {}".format(inc,file_name[1]))
    imapre(file_name)

def drop_in_list_box(event,incr):
    lista.insert("end","{}]".format(incr))
    for i in range(0,5):
        lista.insert("end",event[i])
#inc += 1
    del output[:]

root = TkinterDnD.Tk()
root.geometry("800x500")

listb = tk.Listbox(root, height=8, width=5,selectmode=tk.SINGLE,bg="#f4c2c2")
listb.pack(fill=tk.X)
listb.drop_target_register(DND_FILES)
listb.dnd_bind("<<Drop>>", drop_inside_list_box)

lista = tk.Listbox(root, fg="#ffff00" ,height = 20,selectmode=tk.SINGLE,bg="#006994")
lista.pack(fill=tk.X)
lista.drop_target_register(DND_FILES)
listb.dnd_bind("<<Enter>>", drop_in_list_box)


root.mainloop()


	