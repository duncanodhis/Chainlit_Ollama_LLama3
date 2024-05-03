Chainlit Chatbot

This is a Chainlit-based chatbot application. It uses the Chainlit framework to create a conversational interface and interacts with a backend service to generate responses.

Getting Started

To run this application, ensure you have Python 3.10 or later installed.
Installing Dependencies

To install the required Python packages, use the following command:


pip install -r requirements.txt

Running the Application
To start the Chainlit application, navigate to the directory containing app.py and run:

chainlit run app.py


Docker Setup
If you prefer to use Docker, follow these steps:

Build the Docker Image:
docker build -t chainlit_app -f Dockerfile .

Run the Docker Container:
docker run -p 8000:8000 chainlit_app
