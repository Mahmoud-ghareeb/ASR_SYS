# Detailed README for Automated Speech Recognition (ASR) Pipeline

## Overview

This repository provides a pipeline for transcribing audio files and performing natural language analysis on the transcribed text. The pipeline uses the following services:

1. **Transcription Service (`TranscripeService`)**: Converts audio to text.
2. **Language Model Service (`LLMService`)**: Sends the transcribed text to an OpenAI model to perform further analysis, such as sentiment analysis, named entity recognition, summarization, and topic categorization.
3. **Output**: The results are saved as a JSON file with structured data.

## Project Structure

## Project Structure

/project-root
├── configs
│   └── config.yaml  # Contains the initial prompt
├── src
│   ├── transcripe.py  # Transcription service
│   └── llm.py  # Language model service
├── test_audios  # Directory for storing input audio files
├── output.json  # Output JSON file with analysis results
├── README.md  # Project documentation
├── requirements.txt  # Project dependencies
└── main.py  # Main script to run the pipeline



## Installation

### Prerequisites

Before running this pipeline, make sure you have the following installed:

1. Python 3.10+ 
2. Required Python packages (listed in `requirements.txt`)

### Install Dependencies

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/Mahmoud-ghareeb/ASR_SYS.git
    cd ASR_SYS
    ```

2. Install the necessary dependencies.

    ```bash
    pip install -r requirements.txt
    ```
3. export neccessary keys.
    ```bash
    export SAMBANOVA_API_KEY=*********
    export OPENAI_API_KEY=**********
    ```

## How It Works

### 1. **Transcription Service (`TranscripeService`)**:
The `TranscripeService` uses Whisper to transcribe the audio into text. This service accepts the path to an audio file (e.g., `.wav`, `.mp3`, etc.) and returns the transcribed text.

### 2. **LLM Service (`LLMService`)**:
The `LLMService` takes the transcribed text and sends it to an OpenAI model or Sambanova model for further analysis. It can perform the following:

- **Sentiment Analysis**: Detects the overall sentiment (e.g., positive, negative, neutral).
- **Named Entity Recognition (NER)**: Extracts key entities such as names, places, dates, etc.
- **Topic Categorization**: Classifies the text into predefined categories (e.g., Family, Marriage, Politics).
- **Summarization**: Provides a concise summary of the transcript.

### 3. **Pipeline Execution**:
The main class, `PipeLine`, integrates the transcription and analysis process. It:

- Accepts the path of an audio file.
- Transcribes the audio into text using `TranscripeService`.
- Sends the transcribed text to `LLMService` for further processing.
- Saves the resulting analysis as a JSON file in a specified output path.

## Usage

### Running the Pipeline

To run the pipeline, simply execute the `main.py` script. This script will:

1. Load the audio file from a specified path.
2. Perform transcription and analysis.
3. Save the output to a JSON file.

#### Example:

```bash
python main.py
```
