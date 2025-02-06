# js-fiLter.py

### JavaScript URL Extractor

`js-fiLter.py` is a Python-based tool designed to extract and filter JavaScript file URLs from raw input data. This tool is useful for **bug bounty hunters, penetration testers, and security researchers** who need to collect JavaScript files for analysis.

## Features

✅ Extracts `.js` file URLs from input files  
✅ Supports filtering URLs based on a specific pattern  
✅ Saves extracted URLs to an output file  
✅ Includes a **verbose mode** for detailed output  
✅ Displays a **banner** with tool credits  

## Installation

Ensure you have **Python 3** installed on your system. You can install the required dependencies using:

```bash
pip install -r requirements.txt  # If there are any dependencies
```

## Usage

Run the script with the following options:

```bash
python3 js-fiLter.py -i input.txt -js output.txt -f example.com -v
```

### Arguments:

| Flag | Description |
|------|-------------|
| `-i, --input_file` | Path to the input file containing URLs (**Required**) |
| `-js, --js_output` | Path to the output file for extracted `.js` URLs (**Required**) |
| `-f, --filter` | (Optional) Filter for URLs containing a specific pattern |
| `-v, --verbose` | (Optional) Enable verbose output |

### Example Usage:

Extract JavaScript files and save to `jsfiles.txt`:
```bash
python3 js-fiLter.py -i urls.txt -js jsfiles.txt
```

Extract `.js` URLs containing `example.com` and enable verbose mode:
```bash
python3 js-fiLter.py -i urls.txt -js jsfiles.txt -f example.com -v
```

## Output
The extracted `.js` URLs are saved to the specified output file, making it easy for further processing.

## About

📌 **Author:** SecBeast  
📌 **License:** MIT  
📌 **Purpose:** This tool is designed for reconnaissance and bug bounty hunting. Use it responsibly! 🚀

