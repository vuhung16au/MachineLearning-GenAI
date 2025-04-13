import os
import argparse
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_file, output_folder, pages_per_split):
    reader = PdfReader(input_file)
    total_pages = len(reader.pages)
    base_name = os.path.splitext(os.path.basename(input_file))[0]

    for start_page in range(0, total_pages, pages_per_split):
        writer = PdfWriter()
        end_page = min(start_page + pages_per_split, total_pages)
        for page in range(start_page, end_page):
            writer.add_page(reader.pages[page])

        output_file = os.path.join(output_folder, f"{base_name}-{start_page + 1:02d}.pdf")
        with open(output_file, "wb") as output_pdf:
            writer.write(output_pdf)

def main():
    parser = argparse.ArgumentParser(
        description="Split PDF files into smaller PDFs.",
        add_help=True  # This ensures --help or -h is included by default
    )
    parser.add_argument("--input-folder", "-i", type=str, default="./input", help="Folder containing input PDF files.")
    parser.add_argument("--output-folder", "-o", type=str, default="./output", help="Folder to save splitted PDF files.")
    parser.add_argument("--number-of-pages", "-n", type=int, default=1, help="Number of pages per splitted PDF file.")
    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder
    pages_per_split = args.number_of_pages

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(".pdf"):
            input_file = os.path.join(input_folder, file_name)
            split_pdf(input_file, output_folder, pages_per_split)

if __name__ == "__main__":
    main()