# DialogueDepot AI Flask API

Welcome to the Flask API of DialogueDepot AI! This API serves as the backend for generating AI responses in real-time within the DialogueDepot AI chat application.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Dockerization](#dockerization)
- [Tech Stack](#tech-stack)
- [Model](#model)
- [Contact](#contact)

## Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the `dialogue-depot-flask-api` directory:

   ```bash
   cd dialogue-depot-flask-api
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the Flask API locally, execute the following command:

```bash
python app.py
```

The API will be accessible at `http://localhost:8000`.

## Endpoints

- **POST /:**
  - Generates AI responses based on user input.

- **POST /api:**
  - Accepts JSON input for generating AI responses.

## Dockerization

The API can be containerized using Docker. Ensure Docker is installed, then build the Docker image:

```bash
docker build -t dialogue-depot-flask-api .
```

Run the Docker container:

```bash
docker run -p 8000:8000 dialogue-depot-flask-api
```

## Tech Stack

- Python
- Flask
- Transformers Library
- Docker

## Model

The API utilizes a pre-trained language model from the Hugging Face Transformers library for generating natural language responses.

## Contact

For inquiries or support, please contact:

- Email: [your-email@example.com](mailto:support@hacktivspace.com)
- GitHub: [Your GitHub Username](https://github.com/HacktivSpaceCommunity)
