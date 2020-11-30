import streamlit as st
import io
import requests
from PIL import Image, ImageDraw


st.title('顔認識アプリ')

subscription_key ='fc6c5855a8464e1bb9b6fdd0ee325ef2'
assert subscription_key
face_api_url = 'https://20201130yyokotin.cognitiveservices.azure.com/face/v1.0/detect'

headers = {
    'Content-Type' : 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key
}

params = {
    'returnFaceId': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
}


uploaded_file = st.file_uploader("Choose an image...", type='jpg')
if uploaded_file is not None:
    img = Image.open(uploaded_file)gi
    with io.BytesIO() as output:
        img.save(output, format="JPEG")
        binary_image = output.getvalue()



    res = requests.post(face_api_url, params=params, headers=headers, data=binary_image)
    results = res.json()
    for result in results:
        rect = result['faceRectangle']

        draw = ImageDraw.Draw(img)
        draw.rectangle([(rect['left'], rect['top']),(rect['left']+rect['width'], rect['top']+rect['height'])], fill=None, outline='green', width=5)

    st.image(img, caption='Uploaded Image.', use_columns_width=True)


