import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

def add_text_to_image(text):
    # Open the JPEG image
    image = Image.open("invitation_card.jpeg")

    width, height = image.size

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Define the font for the text
    font = ImageFont.truetype("helvetica.ttf", 35)

    # Specify the text and position
    text_width, text_height = draw.textsize(text, font)  # Get the width and height of the text

    # Calculate the x-coordinate to center the text
    x = (width - text_width) / 2
    y = 730  # Adjust the y-coordinate as needed

    # Add the text to the image
    draw.text((x, y), text, font=font, fill=(169, 104, 0))

    return image

st.title("Add Invitees")

text = st.text_input("Enter the name of the invitee (Ex - Mr & Mrs Ranasinghe & family):")

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
modified_images_folder = os.path.join(downloads_path, "Modified Invitations")
if not os.path.exists(modified_images_folder):
    os.makedirs(modified_images_folder)

output_path = os.path.join(modified_images_folder, f"{text}.jpeg")

if st.button("Add the name"):
    if text:
        modified_image = add_text_to_image(text)
        
        # Display the modified image
        st.image(modified_image, caption="Modified Invitation")
        
        # Save the image to the specified folder
        modified_image.save(output_path)
        
        # Create a download button
        with open(output_path, "rb") as file:
            st.download_button(
                label="Download the modified invitation",
                data=file,
                file_name=f"{text}.jpeg",
                mime="image/jpeg"
            )
    else:
        st.write("Please enter text.")