# Sci-ImageMiner Annotation Tool

## Description

The Sci-ImageMiner Annotation Tool is a web-based application designed to streamline the annotation of domain-specific datasets. It provides an intuitive interface for managing progressive annotation tasks, ensuring consistent labeling, and supporting multiple users.

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required dependencies:

```sh
pip install -r requirements.txt
```

## Adding User Credentials

User credentials are managed through a **CSV** configuration file in the root folder.

1. Open the credentials file `users.csv`:

2. Add a new user entry following the existing format:

3. Save the file before launching the application.

## Launch Application

Start the application using:

```sh
streamlit run app.py
```

Once the server is running, open your browser and navigate to (change the port as shown on the terminal):

```text
http://localhost:8080
```

Log in using your assigned credentials to begin annotating.
