import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

def add_text_to_image(text):
    # Open the JPEG image
    image = Image.open("homecoming.jpg")
    width, height = image.size
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    # Define the font for the text
    font = ImageFont.truetype("helvetica.ttf", 40)
    # Specify the text and position
    left, top, right, bottom = font.getbbox(text)
    text_width = right - left
    # Calculate the x-coordinate to center the text
    x = (width - text_width) / 2
    y = 750  # Adjust the y-coordinate as needed
    # Add the text to the image
    draw.text((x, y), text, font=font, fill=(169, 104, 0))
    return image

st.title("Add Invitees - Homecoming")
text = st.text_input("Enter the name of the invitee (Ex - Mr & Mrs Ranasinghe & family):")

if st.button("Preview"):
    if text:
        modified_image = add_text_to_image(text)
        
        # Display the modified image
        st.image(modified_image, caption="Modified Invitation")
        
        # Convert the image to bytes
        img_byte_arr = io.BytesIO()
        modified_image.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        
        # Create a download button
        st.download_button(
            label="Download the Invitation",
            data=img_byte_arr,
            file_name=f"{text}.jpeg",
            mime="image/jpeg"
        )
    else:
        st.write("Please enter text.")
