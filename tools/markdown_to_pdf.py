#!/usr/bin/env python3
"""Minimal Markdown-to-PDF converter using ReportLab.

Usage: python markdown_to_pdf.py input.md output.pdf

This script strips basic markdown markers and writes plain text to PDF.
It's intentionally lightweight to avoid heavy dependencies.
"""
import sys
import textwrap
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def md_to_text(md):
    lines = []
    for raw in md.splitlines():
        line = raw.strip()
        # headings: remove leading #
        if line.startswith('#'):
            line = line.lstrip('#').strip().upper()
        # remove simple markdown list markers
        if line.startswith('- '):
            line = '• ' + line[2:]
        # code fence markers -> skip
        if line.startswith('```'):
            continue
        lines.append(line)
    return '\n'.join(lines)


def write_pdf(text, out_path):
    c = canvas.Canvas(out_path, pagesize=A4)
    width, height = A4
    left = 50
    right = width - 50
    y = height - 50
    wrap_width = 90
    for paragraph in text.split('\n\n'):
        for line in paragraph.splitlines():
            if not line:
                y -= 12
                continue
            wrapped = textwrap.wrap(line, wrap_width)
            for w in wrapped:
                if y < 60:
                    c.showPage()
                    y = height - 50
                c.setFont('Helvetica', 10)
                c.drawString(left, y, w)
                y -= 14
        y -= 8
    c.save()


def main():
    if len(sys.argv) != 3:
        print('Usage: markdown_to_pdf.py input.md output.pdf')
        sys.exit(2)
    inp, outp = sys.argv[1], sys.argv[2]
    with open(inp, 'r', encoding='utf-8') as f:
        md = f.read()
    text = md_to_text(md)
    write_pdf(text, outp)


if __name__ == '__main__':
    main()
