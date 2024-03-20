# Project Name

## Introduction

This project aims to create a workflow that involves reading a PDF file, converting it to text, splitting the text, embedding it into vector format, saving it to a vector database, and then allowing users to input text, check for similarity, and return relevant results. 

## Requirements

- Python 3.10
- Packages listed in requirements.txt

## Installation

### Step 1: Create and activate a new environment

```bash
python3.10 -m venv venv
venv/Scripts/activate
```

### Step 2: Install required packages

```bash
pip install -r requirements.txt
```

### Step 3: Create a .env file with your API key

Create a file named `.env` in the root directory of your project and add the following line:

```
GOOGLE_API_KEY = 'Your api key'
```

## Workflow

1. **Read PDF and Convert to Text**: The project reads a PDF file and converts it into text format.
   
2. **Text Splitting**: The text is split into smaller segments for further processing.

3. **Embedding**: The text segments are embedded into vector format using appropriate techniques.

4. **Save to Vector Database**: The vectors representing the text segments are saved to a database for easy retrieval.

5. **Context and Prompt Template**: Templates are created to provide context and prompts for user interaction.

6. **User Input and Similarity Check**: Users input text, which is checked for similarity against the stored vectors, and relevant results are returned.

## Usage

1. Ensure the environment is activated.
2. Run the necessary scripts for reading PDF, text processing, and vector embedding.
3. Provide user interface or API endpoints for user interaction.

## Contributing

Contributions are welcome!
