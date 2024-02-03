import streamlit as st
# Import any other libraries you need to process your PDFs. For example, PyPDF2.

def main():
    st.title("PDF Upload Example")

    # Create a file uploader widget
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        pdf_file = BytesIO(bytes_data)
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        
        st.write(f"Number of pages in the PDF: {pdf_reader.numPages}")
        
        # Display text of the first page as an example
        page = pdf_reader.getPage(0)
        page_text = page.extractText()
        st.write(page_text)

if __name__ == "__main__":
    main()
