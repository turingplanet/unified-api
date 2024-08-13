# How to Run This Project
This document provides the necessary steps to set up and run the project. Please follow the instructions carefully to ensure everything works smoothly.

## Setup

Before running the project, you need to set up the environment. Please follow the instructions in [this document](https://github.com/turingplanet/python-project-setup-tutorial/blob/main/comprehensive_set_up.md#poetry-project-setup) to install and configure Poetry.

## Configuration

1. Modify the `secret.yml` file in the project root:
   - Open [secret.yml](./secret.yml)
   - Replace the default token with your OpenAI API key.

## Running the Project

After setting up your environment and configuring the necessary files, you can start the project using the following commands:

1. Install project dependencies:
   ```bash
   poetry install
   ```
2. To generate the vector store:
   ```bash
   poetry run python3 rag_demo/vector_store_generator.py
   ```
3. To start the unified API server:
   ```bash
   poetry run python3 unified_api/unified_api_server.py
   ```
Ensure you execute these commands from the root of the project directory where the pyproject.toml file is located.



