The number of layers and the types of layers you include in between are up to you. You may wish to experiment with:

    different numbers of convolutional and pooling layers
    different numbers and sizes of filters for convolutional layers
    different pool sizes for pooling layers
    different numbers and sizes of hidden layers
    dropout


First working Model:
- Epochs: 3 (mainly to reduce time)
- convolutional Filter AMT = 32, SIZE = (3,3)
- Pool Size (2,2)
- 

accuracy: 0.8270 - loss: 0.5802

Changin the FILTER_AMT and KERNEL
- 16, (2,2)
accuracy: 0.4738 - loss: 1.0156

increasing epochs to 8., 
accuracy: 0.4643 - loss: 0.9452
returning to  Filter AMT = 32, SIZE = (3,3)
accuracy: 0.4730 - loss: 0.9457

increasing the number of categories to 21
accuracy: 0.4417 - loss: 1.7443

additional hidden layer with dropout
accuracy: 0.1508 - loss: 2.1859
--> removed

hidden layer, change of 1st parameter to 128
accuracy: 0.1515 - loss: 2.1903
    1st parameter to 64 ->
accuracy: 0.1497 - loss: 2.1897

Filter AMT back to 32
-> no real improvement

Image Size too 50x50
--> no improvements


OUtput Layer, sigmoid activation
--> no improvements

hidden layer to 8
--> no improv


added second hidden layer 1st:: 64, second: 32

tried changing the image size again, no improvements

working with 20 categories now
accuracy: 0.0811 - loss: 2.8558


deleted second hidden layer
1st hidden layer up to 128
accuracy: 0.3673 - loss: 1.9467

NUM_Cat= 15, EPOCHS = 8
--> hidden layer to 512
    big improvements here
accuracy: 0.9385 - loss: 0.2552
    compare, 128 inhidden layer: accuracy: 0.0951 - loss: 2.6157

Second hidden layer, at 64
accuracy: 0.9049 - loss: 0.3259

2nd hidden to 256
accuracy: 0.8824 - loss: 0.4484

to 32?
really bad

to 512?
accuracy: 0.9392 - loss: 0.2340
--> still just as good as without 2nd layer

removed 2nd hidden layer
first hidden layer to 1024
accuracy: 0.9451 - loss: 0.2642

POOL_SIZE TO 3,3 from 2,2
-> improved tempo 

2nd convo layer?
    half filter amt?
    no improv