from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.datasets import mnist
from keras.optimizers import SGD
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train, y_train)
kk=x_train.shape
print(kk)
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print(x_test, y_test)

model= Sequential()
model.add (Dense(input_dim=28*28,output_dim=500))
model.add(Activation('sigmoid'))
model.add(Dense(output_dim=500))
model.add(Activation('sigmoid'))
model.add(Dense(output_dim=10))
model.add(Activation('sigmoid'))
model.compile(loss='mse',optimizer=SGD(lr=0.1),metrics=['accuracy'])

a=0
for x0 in x_train:
	y=y_train[a]
	x = x0.reshape((1,784))
	k=x.shape
	print(k)
	model.fit(x,y,batch_size=100,nb_epoch=20)
	score=model.evaluate(x_text,y_test)
	print(score[0])
	print(score[1])
	a=a+1