
# Happy Dataset Summarizer
![alt text](https://github.com/azario0/happy-dataset-summarizer/blob/main/logo.png)

## Overview

Happy Dataset Summarizer is a Python tool that generates comprehensive reports for CSV datasets, providing insights into column structures, unique values, and optional descriptive statistics to ask a LLM .

## Installation

```bash
pip install happy-dataset-summarizer
```

## Usage

### Command Line Interface

```bash
# Basic usage
happy-dataset-summarizer your_dataset.csv

# Include descriptive statistics
happy-dataset-summarizer your_dataset.csv -d

# Specify custom output file
happy-dataset-summarizer your_dataset.csv -o custom_report.txt
```

### Python Import

```python
from happy_dataset_summarizer import generate_report

generate_report('your_dataset.csv', include_describe=True)
```

## Features

- List dataset columns
- Display first three rows
- Analyze unique values in categorical columns
- Check for null values
- Optional descriptive statistics

## Requirements

- Python 3.7+
- pandas

## License

MIT
