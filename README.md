# QuantGPT: Financial Report Analysis Engine

![Project Status](https://img.shields.io/badge/status-active-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

QuantGPT is an AI-powered financial report analysis engine designed to efficiently parse and analyze large-scale financial documents, such as 300-page annual reports. By leveraging advanced NLP techniques, Langchain, and ChromaDB, QuantGPT allows for vectorized querying of financial statements, offering users precise, real-time insights into financial data.

This project deploys a Streamlit interface, integrated with the OpenAI API, to provide a seamless, interactive platform for financial report extraction and analysis. It offers real-time financial statement parsing, using GPT-4 to enhance financial data comprehension and decision-making.

## Key Features

- **AI Agent**: Utilizes Langchain and ChromaDB for vectorized NLP querying of large financial reports.
- **Streamlit Interface**: Provides an interactive platform for users to query and analyze financial statements in real-time.
- **OpenAI API Integration**: Integrated with GPT-4 for advanced natural language processing, extracting precise financial insights.
- **Financial Statement Analysis**: Automated extraction and summarization of key financial metrics and statements from reports.

## Technologies Used

- **Python**: The core programming language used for the backend and agent.
- **Langchain**: Manages the document parsing pipeline, vectorizing and analyzing text.
- **ChromaDB**: A vector store used for document embeddings and querying.
- **Streamlit**: Used to build an intuitive user interface for financial statement analysis.
- **GPT-4**: The language model used for processing financial language and extracting insights.
- **PyPDF**: Library used to handle PDF extraction and processing.
- **CryptoDome**: Adds security and cryptographic functionality.

## Code Reference

This project is heavily inspired by [LangchainDocuments](https://github.com/nicknochnack/LangchainDocuments), where similar methods were used to parse documents and apply NLP techniques. 

## Contributing

Feel free to fork this repository, create a branch, and submit a pull request with any features, bug fixes, or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
