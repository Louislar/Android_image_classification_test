"""
可以確認.pb檔案儲存的網路的input層的名子，以及output層的名子
"""


import tensorflow as tf
gf = tf.GraphDef()   
m_file = open('keras_to_tensorflowlite_success/keras_to_tensorflow/checkpoint/minst_trained_model.pb','rb')
gf.ParseFromString(m_file.read())

with open('somefile.txt', 'a') as the_file:
    for n in gf.node:
        the_file.write(n.name+'\n')

file = open('somefile.txt','r')
data = file.readlines()
print ("output name = ")
print (data[len(data)-1])

print ("Input name = ")
file.seek ( 0 )
print (file.readline())