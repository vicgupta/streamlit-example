import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import requests

#https://dl.airtable.com/.attachmentThumbnails/b4cea114fb3157dfb0affbd1bac9f0c9/fc94c3db
im1 = 'https://dl.airtable.com/.attachmentThumbnails/49ab1ed32adabaa49408b3fd81df324c/bd597b11'
im1 = "https://images.pexels.com/photos/10757791/pexels-photo-10757791.jpeg"

post_text = st.text_input ("Enter Post Text: ")

image = Image.open(requests.get(im1, stream=True).raw)

st.image(image, caption='Sunrise by the mountains')

