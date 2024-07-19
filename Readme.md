# AI Blog Generator with CrewAI and Ollama

This is a private fun project created to explore working with Language Models (LLMs), AI Agents, and Docker. The project uses CrewAI to generate blog posts about AI trends, and Ollama for local LLM inference.

## Project Overview

This project demonstrates the use of:
- CrewAI for orchestrating AI agents
- Ollama for running LLMs locally
- Streamlit for creating a simple web interface
- Docker for containerization

## Disclaimer

This is a personal project for learning and experimentation. It is not intended for production use.

## Prerequisites

- Docker
- Python 3.11 (if running locally without Docker)
- Ollama

## Setup and Running

### Setting up Ollama

1. Install Ollama by following the instructions on the [official Ollama website](https://ollama.ai/download).

2. After installation, run the following command to download the OpenHermes model:
   ```
   ollama pull openhermes
   ```

3. Verify the installation by running:
   ```
   ollama list
   ```
   You should see "openhermes" in the list of available models.

### Using Docker

1. Build the Docker image:
   ```
   docker build -t ai-blog-generator .
   ```

2. Run the Docker container:
   ```
   docker run -p 8501:8501 ai-blog-generator
   ```

3. Open your web browser and go to `http://localhost:8501`

### Running Locally

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Project Structure

- `main_crewai.py`: Contains the CrewAI logic for generating blog posts
- `app.py`: Streamlit app for the web interface
- `Dockerfile`: Instructions for building the Docker image
- `requirements.txt`: List of Python dependencies

## Learning Outcomes

This project has been an excellent opportunity to:
- Understand how to work with AI agents using CrewAI
- Set up and use Ollama for local LLM inference
- Create a simple web interface with Streamlit
- Containerize a Python application using Docker

## Future Improvements

- Enhance the AI agents' capabilities
- Improve the user interface
- Add more customization options for blog generation
- Experiment with different Ollama models

## Troubleshooting

If you encounter issues with Ollama or the LLM not responding:
1. Ensure Ollama is running in the background
2. Check if the OpenHermes model is properly downloaded
3. Restart the Ollama service if necessary

## Acknowledgements

This project uses the following open-source libraries and tools:
- CrewAI
- Ollama
- Streamlit
- Langchain

## License

This project is open source and available under the [MIT License](LICENSE).