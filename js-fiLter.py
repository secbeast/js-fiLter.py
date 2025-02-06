#!/usr/bin/env python3
import argparse
import re
import sys
import json
import csv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Banner and Tool Info
banner = """
     ██╗███████╗    ███████╗██╗██╗     ████████╗███████╗██████╗
     ██║██╔════╝    ██╔════╝██║██║     ╚══██╔══╝██╔════╝██╔══██╗
     ██║███████╗    █████╗  ██║██║        ██║   █████╗  ██████╔╝
██   ██║╚════██║    ██╔══╝  ██║██║        ██║   ██╔══╝  ██╔══██╗
╚█████╔╝███████║    ██║     ██║███████╗   ██║   ███████╗██║  ██║
 ╚════╝ ╚══════╝    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                    Code by SecBeast
"""

# Function to display the banner first
def show_banner():
    print(banner)

# Function to extract and filter URLs
def extract_js(input_file, js_output_file, filter_pattern=None, verbose=False, output_format='text'):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
            if verbose:
                logging.info(f"Read {len(lines)} lines from '{input_file}'")
    except FileNotFoundError:
        logging.error(f"Input file '{input_file}' not found.")
        sys.exit(1)

    js_urls = []
    for line in lines:
        if '.js' in line:
            match = re.search(r'(https?://\S+\.js)', line)
            if match:
                js_url = match.group(0)
                if filter_pattern and filter_pattern not in js_url:
                    continue
                js_urls.append(js_url)
                if verbose:
                    logging.info(f"Extracted URL: {js_url}")

    if output_format == 'json':
        with open(js_output_file, 'w') as js_file:
            json.dump({"urls": js_urls}, js_file, indent=4)
    elif output_format == 'csv':
        with open(js_output_file, 'w', newline='') as js_file:
            writer = csv.writer(js_file)
            writer.writerow(["URL"])  # Header
            for url in js_urls:
                writer.writerow([url])
    else:  # Default to text format
        with open(js_output_file, 'w') as js_file:
            for url in js_urls:
                js_file.write(url + '\n')

    if verbose:
        logging.info(f"Extracted {len(js_urls)} .js URLs")
        logging.info(f"Saved to '{js_output_file}'")

# Main Function
def main():
    show_banner()

    parser = argparse.ArgumentParser(description="Pure.js Extractor", epilog="Code by SecBeast")
    parser.add_argument('-i', '--input_file', required=True, help="Path to the input file containing URLs.")
    parser.add_argument('-js', '--js_output', required=True, help="Path to the output file for .js URLs.")
    parser.add_argument('-f', '--filter', help="Filter for URLs containing a specific pattern.")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose output.")
    parser.add_argument('-o', '--output_format', choices=['text', 'json', 'csv'], default='text', help="Output format (text, json, or csv).")

    args = parser.parse_args()

    extract_js(args.input_file, args.js_output, args.filter, args.verbose, args.output_format)

if __name__ == "__main__":
    main()
