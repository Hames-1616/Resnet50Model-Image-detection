import io
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from PIL import Image
import matplotlib.pyplot as plot
from skimage.io import imread

async def predict(file):
    model = ResNet50(weights='imagenet')
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert('RGB')
    img = img.resize((224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    decode_preds=decode_predictions(preds, top=3)[0]
    result = []
    for  label, description, probability in decode_preds:
        result.append({
            "label": label,
            "description": description,
            "probability": float(probability)
        })
    
    return result
