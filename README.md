# PDF to Audio Converter

This project is a web application that converts PDF files to audio files using Flask, PyPDF2, and gTTS (Google Text-to-Speech). It allows users to upload a PDF file, extracts the text from the PDF, converts it into speech, and provides a downloadable MP3 file.

## Features

- Upload a PDF file.
- Extract text from the PDF.
- Convert the extracted text into an MP3 audio file.
- Download the MP3 file.

## Technologies Used

- **Python**: The backend language.
- **Flask**: A lightweight web framework for Python.
- **PyPDF2**: Library for reading PDF files.
- **gTTS**: Google Text-to-Speech for converting text to speech.
- **HTML/CSS/JavaScript**: For the frontend and user interaction.

## Installation

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/pdf-to-audio-converter.git
   cd pdf-to-audio-converter
   ```

2. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install flask gtts PyPDF2
   ```

3. **Run the Application**

   Start the Flask server:

   ```bash
   python app.py
   ```

   The application will be available at `http://127.0.0.1:5000/` in your web browser.

## Usage

1. **Upload a PDF File**

   - Navigate to `http://127.0.0.1:5000/`.
   - Click the "Choose File" button to select a PDF file from your computer.
   - Click "Convert to Audio" to upload and process the file.

2. **Download the MP3 File**

   - After processing, a link will appear allowing you to download the MP3 file containing the spoken version of the PDF's text.

## Project Structure

- `app.py`: The Flask application script.
- `static/style.css`: Contains the CSS styles for the frontend.
- `static/script.js`: JavaScript file for handling form submission and showing the loading spinner.
- `templates/index.html`: The main HTML template for the application.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements. Please ensure that your contributions follow the project’s coding style and include tests where applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF text extraction.
- [gTTS](https://pypi.org/project/gTTS/) for text-to-speech conversion.
- [CSS Loading Spinner](https://loading.io/) for the loading spinner design.

```

### Instructions to Use

1. **Clone the Repository**: Copy the URL of your GitHub repository and use `git clone` to get the project onto your local machine.
2. **Install Dependencies**: Make sure you have Python installed, then install the necessary packages using `pip`.
3. **Run the Application**: Execute `python app.py` to start the server and access the app via your web browser.
