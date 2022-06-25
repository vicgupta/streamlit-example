import streamlit as st
from PIL import Image, ImageDraw, ImageFont
#https://dl.airtable.com/.attachmentThumbnails/b4cea114fb3157dfb0affbd1bac9f0c9/fc94c3db
im1 = 'https://dl.airtable.com/.attachmentThumbnails/49ab1ed32adabaa49408b3fd81df324c/bd597b11'

post_text = st.text_input ("Enter Post Text: ")

im = Image.open("https://dl.airtable.com/.attachmentThumbnails/1fb3bfc74fd118479c8d3b4392a0c20f/2967c81a" + ".png")
