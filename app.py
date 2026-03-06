import cv2
import fitz 
import easyocr
import numpy as np
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Smart Document Scanner", page_icon="📄")

@st.cache_resource
def load_ocr_model(langs):
    return easyocr.Reader(list(langs), gpu=False)

def preprocess_image(image_array):
    if len(image_array.shape) == 3 and image_array.shape[2] == 4:
        gray = cv2.cvtColor(image_array, cv2.COLOR_RGBA2GRAY)
    elif len(image_array.shape) == 3:
        gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    else:
        gray = image_array
        
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_gray = clahe.apply(gray)
    
    img_resized = cv2.resize(enhanced_gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    return img_resized

def extract_text_from_image(img_array, reader):
    preprocessed = preprocess_image(img_array)
    result = reader.readtext(preprocessed, detail=0, paragraph=True, adjust_contrast=True)
    text = "\n".join(result)
    return text.strip()

def main():
    st.title(" Smart Document Scanner")

    lang_choice = st.radio(
        "Select Document Language:", 
        ("English", "Arabic", "Both (Arabic & English)"), 
        horizontal=True
    )

    if lang_choice == "English":
        langs = ('en',)
    elif lang_choice == "Arabic":
        langs = ('ar',)
    else:
        langs = ('ar', 'en')

    reader = load_ocr_model(langs)

    upload = st.file_uploader(
        "Upload an image (jpg, png, jpeg, webp) or PDF", 
        type=["jpg", "png", "jpeg", "webp", "pdf"]
    )

    if upload is not None:
        if st.button("Start Processing"):
            if upload.type == "application/pdf":
                try:
                    doc = fitz.open(stream=upload.read(), filetype="pdf")
                    all_text = ""
                    for page_num in range(len(doc)):
                        page = doc.load_page(page_num)
                        pix = page.get_pixmap()
                        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                        img_array = np.array(img)
                        
                        st.image(img_array, caption=f"PDF Page {page_num + 1}", use_container_width=True)
                        with st.spinner(f"Extracting text from PDF page {page_num + 1}..."):
                            all_text += extract_text_from_image(img_array, reader) + "\n\n"
                    text = all_text
                except Exception as e:
                    st.error(f"Error reading PDF: {e}")
                    text = ""
            else:
                img = Image.open(upload)
                img_array = np.array(img)
                st.image(img_array, caption="Uploaded Image", use_container_width=True)
                with st.spinner("Extracting text from your image..."):
                    text = extract_text_from_image(img_array, reader)

            if 'text' in locals() and text:
                st.subheader(" Extracted Text")
                st.text_area("Your text here:", text, height=300)
                st.download_button("Download Text", text, file_name="extracted_text.txt")
            elif 'text' in locals() and not text:
                st.warning("No text detected! Try a clearer image or higher resolution.")

if __name__ == "__main__":
    main()