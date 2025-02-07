#!/usr/bin/env python3
import argparse
import re
import sys
import json
import csv
import logging

# Configure logging to stderr to avoid interfering with stdout
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stderr)

banner = """
     ██╗███████╗    ███████╗██╗██╗     ████████╗███████╗██████╗
     ██║██╔════╝    ██╔════╝██║██║     ╚══██╔══╝██╔════╝██╔══██╗
     ██║███████╗    █████╗  ██║██║        ██║   █████╗  ██████╔╝
██   ██║╚════██║    ██╔══╝  ██║██║        ██║   ██╔══╝  ██╔══██╗
╚█████╔╝███████║    ██║     ██║███████╗   ██║   ███████╗██║  ██║
 ╚════╝ ╚══════╝    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
            [Code by SecBeast]  [Version 1.0]
             [Defronix Student DCSP BATCH-3]
"""

def show_banner():
    print(banner, file=sys.stderr)  # Print banner to stderr

def extract_js(input_file, filter_pattern=None, verbose=False):
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
    return js_urls

def output_urls(js_urls, output_format):
    if output_format == 'json':
        print(json.dumps({"urls": js_urls}, indent=4))
    elif output_format == 'csv':
        writer = csv.writer(sys.stdout)
        writer.writerow(["URL"])
        for url in js_urls:
            writer.writerow([url])
    else:  # Default to text format
        for url in js_urls:
            print(url)

def main():
    show_banner()

    parser = argparse.ArgumentParser(description="Pure.js Extractor", epilog="Code by SecBeast")
    parser.add_argument('-i', '--input_file', required=True, help="Path to the input file containing URLs.")
    parser.add_argument('-js', '--js_output', help="Optional: Save URLs to a file instead of stdout.")
    parser.add_argument('-f', '--filter', help="Filter for URLs containing a specific pattern.")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose output.")
    parser.add_argument('-o', '--output_format', choices=['text', 'json', 'csv'], default='text', help="Output format.")

    args = parser.parse_args()

    js_urls = extract_js(args.input_file, args.filter, args.verbose)

    if args.js_output:
        # Save to file
        with open(args.js_output, 'w') as f:
            if args.output_format == 'json':
                json.dump({"urls": js_urls}, f, indent=4)
            elif args.output_format == 'csv':
                writer = csv.writer(f)
                writer.writerow(["URL"])
                for url in js_urls:
                    writer.writerow([url])
            else:
                for url in js_urls:
                    f.write(url + '\n')
        if args.verbose:
            logging.info(f"URLs saved to {args.js_output}")
    else:
        # Print to stdout for piping
        output_urls(js_urls, args.output_format)

if __name__ == "__main__":
    main()
