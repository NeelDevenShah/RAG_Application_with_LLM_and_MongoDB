# RAG App

## Overview

This RAG (Retrieval-Augmented Generation) app is designed to provide answers for a given airline review dataset using the RAG model. The app connects to the Hugging Face API to access and utilize the necessary tokens for generating responses.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/rag-app.git`
2. Navigate to the project directory: `cd rag-app`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Ensure that the airline review dataset is available in the specified format.
2. Start the app by running the main script: `python main.py`
3. Access the app through the provided URL: `http://localhost:5000`
4. Enter a query or select a review from the dataset.
5. The app will utilize the RAG model and the connected and used token from Hugging Face to generate an answer based on the query or selected review.

## Configuration

- The Hugging Face API token should be stored in the `config.ini` file.
- Additional configuration options can be modified in the `config.ini` file, such as the dataset path and model parameters.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- This app utilizes the RAG model from Hugging Face (https://huggingface.co/).
- The airline review dataset used in this app is sourced from [source-name] (provide appropriate attribution).
