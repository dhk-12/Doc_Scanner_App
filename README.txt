# 📄 Smart Document Scanner (OCR)

A powerful and user-friendly web application built with Streamlit that extracts text from images and PDF documents using Optical Character Recognition (OCR). The app leverages EasyOCR for high-accuracy text extraction and OpenCV for advanced image preprocessing.

## ✨ Features
- **Multi-Format Support:** Upload images (`JPG`, `PNG`, `JPEG`, `WEBP`) or `PDF` files.
- **Language Selection:** Choose between English, Arabic, or a combination of both for optimized scanning accuracy.
- **Advanced Image Preprocessing:** Uses OpenCV (Grayscale conversion, CLAHE contrast enhancement, and resizing) to improve OCR results on low-quality or low-contrast documents.
- **PDF Processing:** Automatically converts PDF pages to images and extracts text page by page without needing external tools like Poppler.
- **Downloadable Output:** Export the extracted text easily as a `.txt` file.

## 🛠️ Tech Stack
- **[Streamlit](https://streamlit.io/):** For the interactive web interface.
- **[EasyOCR](https://github.com/JaidedAI/EasyOCR):** For Optical Character Recognition.
- **[PyMuPDF (fitz)](https://pymupdf.readthedocs.io/):** For PDF parsing and rendering.
- **[OpenCV](https://opencv.org/):** For image preprocessing and contrast enhancement.

## ⚙️ Installation & Setup

1. **Clone the repository** (or create a new folder and add your script):
   ```bash
   git clone [https://github.com/dhk-12/Doc_Scanner_App.git]
   cd Doc_Scanner_App

2. **Install the required dependencies:**
   It is recommended to use a virtual environment. Install the packages using pip:
   ```bash
   pip install -r requirements.txt

3. **Run the application:**
   ```bash
   streamlit run app.py

## 🚀 How to Use
1. Open the app in your browser (usually `http://localhost:8501`).
2. Select the language of your document (English, Arabic, or Both).
3. Upload an image or a PDF file using the drag-and-drop area.
4. Click on the **Start Processing** button to begin text extraction.
5. Review the extracted text in the text area.
6. Click **Download Text** to save the output locally.