from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import vgg16
from tensorflow.keras.applications.vgg16 import VGG16
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras import backend as K
tf.compat.v1.disable_eager_execution()


def Grad_Cam(model, img, layer_name):
    #  preprocess the input image as vgg16 demands
    x = vgg16.preprocess_input(np.expand_dims(image.img_to_array(img), axis=0))
    pred = model.predict(x)
    
    #  get the softmax output that was predicted as drowning
    drowning = model.output[:, np.argmax(pred[0])]
    #  the name of last_conv_layer is 'block5_conv3', which you can check by using 'model.summary()'
    last_conv_layer = model.get_layer(layer_name)
    #  defining the calculation of the gradient between output of softmax and last_conv_layer
    grads = K.gradients(drowning, last_conv_layer.output)[0]
    pooled_grads = K.mean(grads, axis=(0, 1, 2))
    #  pack up small functions above as a new function, then feed the input image ‘x’
    iterate = K.function([model.input], [pooled_grads, last_conv_layer.output[0]])
    pooled_grads, conv_output = iterate([x])
    
    # weighting all the feature maps of last_conv_layers (in vgg16 we get 512 feature maps)
    for j in range(conv_output.shape[-1]):
        conv_output[:, :, j] *= pooled_grads[j]

    # some processing on heatmap
    heatmap = np.maximum(np.mean(conv_output, axis=-1), 0)
    heatmap /= np.max(heatmap)
    heatmap = np.uint8(255 * cv2.resize(heatmap, (224, 224)))
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    superimposed_img = (np.float32(heatmap) + img)
    return superimposed_img, heatmap

model = VGG16(weights='imagenet')
img_path = "./images/cat_dog.png"
img = image.load_img(img_path, target_size=(224, 224))

superimposed_img, heatmap = Grad_Cam(model, img, "block5_conv3")
cv2.imwrite("./images/heatmap.png", heatmap)
cv2.imwrite("./images/gradcam.png", superimposed_img)