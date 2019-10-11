import tensorflow_hub as hub

# 可复用模型库 TensorFlow Hub
## 来自google的130G文本训练的 文字处理模型:文字转化为向量
embed = hub.load("https://hub.tensorflow.google.cn/google/tf2-preview/gnews-swivel-20dim/1")
embeddings = embed(["cat is on the mat", "dog is in the fog"])
print(embeddings)

