#!/usr/bin/python3

import sys
import os
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    with open(markdown_file, 'r') as f:
        markdown_text = f.read()

    html = markdown.markdown(markdown_text)

    with open(output_file, 'w') as f:
        f.write(html)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_markdown_file> <output_html_file>", file=sys.stderr)
        sys.exit(1)

    input_markdown_file = sys.argv[1]
    output_html_file = sys.argv[2]

    if not os.path.exists(input_markdown_file):
        print(f"Missing {input_markdown_file}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(input_markdown_file, output_html_file)
    sys.exit(0)

