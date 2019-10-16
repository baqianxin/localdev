from __future__ import absolute_import, division, print_function

import os
import tensorflow as tf
import tensorflow_hub as hub

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.compat.v1.enable_eager_execution()

# 加载训练好的模型
file_path = './data/model'
model = tf.keras.models.load_model(file_path + "/iris-model")
# model.summary()

# 定义标签
class_names = ['Iris setosa', 'Iris versicolor', 'Iris virginica']

predict_dataset = tf.convert_to_tensor([
    [5.1, 3.3, 1.7, 0.5, ],
    [5.9, 3.0, 4.2, 1.5, ],
    [6.9, 3.1, 5.4, 2.1]
])

predictions = model(predict_dataset)

for i, logits in enumerate(predictions):
    class_idx = tf.argmax(logits).numpy()
    p = tf.nn.softmax(logits)[class_idx]
    name = class_names[class_idx]
    print("Example {} prediction: {} ({:4.1f}%)".format(i, name, 100*p))


# 加载 影评 模型 
model = tf.keras.models.load_model( "./data/model/imdb_model.h5", custom_objects={'KerasLayer': hub.KerasLayer})
# 解析测试数据集
embed = hub.load("https://hub.tensorflow.google.cn/google/tf2-preview/gnews-swivel-20dim/1")
embeddings = embed(["i love you"])
predictions = model(embeddings)

print(predictions)
