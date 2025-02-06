#!/usr/bin/env python3
import argparse
import re
import sys

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
def extract_js(input_file, js_output_file, filter_pattern=None, verbose=False):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    js_urls = []
    for line in lines:
        if '.js' in line:
            # Use regex to extract only the URL part (after [script] [GET])
            match = re.search(r'(https?://\S+\.js)', line)
            if match:
                js_url = match.group(0)
                if filter_pattern and filter_pattern not in js_url:
                    continue
                js_urls.append(js_url)

    with open(js_output_file, 'w') as js_file:
        for url in js_urls:
            js_file.write(url + '\n')

    if verbose:
        print(f"Extracted {len(js_urls)} .js URLs")
        print(f"Saved to {js_output_file}")

# Main Function
def main():
    # Display the banner first
    show_banner()

    # Argument parser setup
    parser = argparse.ArgumentParser(description="Pure.js Extractor", epilog="Code by SecBeast")
    parser.add_argument('-i', '--input_file', required=True, help="Path to the input file containing URLs.")
    parser.add_argument('-js', '--js_output', required=True, help="Path to the output file for .js URLs.")
    parser.add_argument('-f', '--filter', help="Filter for URLs containing a specific pattern.")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose output.")
    
    # Parse arguments
    args = parser.parse_args()

    # If the arguments are valid, proceed to extract URLs
    if args.input_file and args.js_output:
        extract_js(args.input_file, args.js_output, args.filter, args.verbose)

if __name__ == "__main__":
    main()
