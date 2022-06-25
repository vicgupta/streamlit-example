import streamlit as st
from PIL import Image, ImageDraw, ImageFont


post_text = st.text_input ("Enter Post Text: ")


#font = ImageFont.truetype("Tests/fonts/NotoSans-Regular.ttf", 48)
im = Image.new("RGB", (200, 200), "white")
d = ImageDraw.Draw(im)
d.line(((0, 100), (200, 100)), "gray")
d.line(((100, 0), (100, 200)), "gray")
#d.text((100, 100), "Quick Brown", fill="black", anchor="ms", font=font)
d.text((100, 100), "Quick Brown", fill="black", anchor="ms")
