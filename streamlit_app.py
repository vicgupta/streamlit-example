import streamlit as st
from PIL import Image, ImageDraw, ImageFont
#https://dl.airtable.com/.attachmentThumbnails/b4cea114fb3157dfb0affbd1bac9f0c9/fc94c3db
im1 = 'https://dl.airtable.com/.attachmentThumbnails/49ab1ed32adabaa49408b3fd81df324c/bd597b11'

post_text = st.text_input ("Enter Post Text: ")

im = Image.open(im1)
