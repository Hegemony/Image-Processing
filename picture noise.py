import torch
from torchvision import transforms
from PIL import Image
import numpy as np
import cv2


# 1.1 tensor2Image Image格式进行绘图，展示
tensor1 = torch.randint(0, 255, (681, 1024, 3))
# transform1 = transforms.ToPILImage(mode="RGB")
# image1 = transform1(np.uint8(tensor1.numpy())) # Image接受的图像格式必须为uint8，否则就会报错
# print(tensor1.size())
# print(image1)
# # image.show()
# image1.save("gray.jpg")

# src = np.array(image).astype(np.uint8)  # image: img (PIL Image):
tensor1 = np.uint8(tensor1.numpy())
im = Image.fromarray(tensor1)
im.save("rgb1.jpeg")