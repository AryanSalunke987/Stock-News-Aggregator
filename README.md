# Stock-News-Aggregator

A Python-based web scraping application that collects financial news headlines from **Moneycontrol** and **Economic Times**, processes the extracted information and presents it through an interactive Streamlit interface.

## Overview

The Stock News Aggregator aims to simplify access to financial news by collecting articles from multiple sources in one place. It uses Python's web scraping capabilities to extract relevant news information and structures the collected data for easy viewing and analysis.

## Features

- **Multi-source News Scraping:** Extracts financial news from Moneycontrol and Economic Times.
- **Web Scraping:** Uses BeautifulSoup to parse HTML content and retrieve relevant article information.
- **Data Processing:** Uses Pandas to structure and organise scraped information.
- **Interactive Dashboard:** Displays collected news through a Streamlit interface.
- **CSV Export:** Saves extracted news data in CSV format for offline access.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Requests | Fetching webpage content |
| BeautifulSoup | HTML parsing and web scraping |
| Pandas | Data processing and structuring |
| Streamlit | Interactive user interface |

## Project Structure

```text
Stock-News-Aggregator/
│
├── app.py          # Streamlit application
├── scrapper.py     # Web scraping and data extraction
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/AryanSalunke987/Stock-News-Aggregator.git
```

### 2. Navigate to the project directory

```bash
cd Stock-News-Aggregator
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## How It Works

1. The application sends HTTP requests to the selected financial news websites.
2. BeautifulSoup parses the retrieved HTML content.
3. Relevant news information, including headlines and article details, is extracted.
4. Pandas structures the collected information into a DataFrame.
5. The Streamlit interface displays the aggregated news.
6. The extracted data can be exported into a CSV file.

## Learning Outcomes

Through this project, I explored:

- Practical implementation of web scraping using Python.
- Understanding HTML structures and CSS selectors.
- Working with HTTP requests and webpage responses.
- Extracting and cleaning unstructured web data.
- Processing structured information using Pandas.
- Building a basic interactive application using Streamlit.

## Disclaimer

This project was developed for educational purposes. Website structures and scraping accessibility may change over time. Please respect the respective websites' terms of service and scraping policies.
