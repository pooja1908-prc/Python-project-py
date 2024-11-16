import PyPDF2
import pyttsx3

def pdf_to_audio(pdf_file, start_page=0, end_page=None):
    try:
        # Open the PDF file
        with open(pdf_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            total_pages = len(pdf_reader.pages)

            # Validate page range
            if end_page is None or end_page > total_pages:
                end_page = total_pages
            if start_page < 0 or start_page >= total_pages:
                print("Invalid start page number. Exiting.")
                return

            # Initialize the text-to-speech engine
            speaker = pyttsx3.init()
            speaker.setProperty('rate', 150)  # Set speech rate (words per minute)
            speaker.setProperty('volume', 0.8)  # Set volume (0.0 to 1.0)

            # Extract text and convert to speech
            for page_num in range(start_page, end_page):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                print(f"Reading page {page_num + 1}...\n{text}\n")
                speaker.say(text)

            # Wait for the speech to finish
            speaker.runAndWait()
            speaker.stop()
            print("Audio conversion completed!")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    pdf_file_path = r"C:\Users\Pooja\Downloads\Case study 2.pdf"  
    start_page = 0
    end_page = None               
    pdf_to_audio(pdf_file_path, start_page, end_page)
