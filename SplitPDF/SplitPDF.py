import os
import argparse
import logging
from pypdf import PdfReader, PdfWriter

def setup_logging(log_file):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.getLogger().addHandler(logging.StreamHandler())

def validate_arguments(args):
    if not os.path.isdir(args.input_folder):
        raise ValueError(f"Error: '{args.input_folder}' is not a valid directory.")
    if args.number_of_pages <= 0:
        raise ValueError("Error: Number of pages must be positive.")
    if args.start_index <= 0:
        raise ValueError("Error: Start index must be positive.")
    if any(c in args.prefix for c in r'\/:*?"<>|'):
        raise ValueError("Error: Prefix contains invalid characters.")

def split_pdf(input_file, output_folder, pages_per_split, prefix, start_index, dry_run, force):
    try:
        reader = PdfReader(input_file)
        total_pages = len(reader.pages)
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        prefix = prefix or base_name

        for start_page in range(0, total_pages, pages_per_split):
            writer = PdfWriter()
            end_page = min(start_page + pages_per_split, total_pages)
            for page in range(start_page, end_page):
                writer.add_page(reader.pages[page])

            output_file = os.path.join(output_folder, f"{prefix}-{start_index:03d}.pdf")
            start_index += 1

            if os.path.exists(output_file) and not force:
                logging.warning(f"Output file '{output_file}' exists. Skipping.")
                continue

            if dry_run:
                logging.info(f"Dry run: Would create '{output_file}' with pages {start_page + 1}-{end_page}.")
                continue

            with open(output_file, "wb") as output_pdf:
                writer.write(output_pdf)
                logging.info(f"Created '{output_file}' with pages {start_page + 1}-{end_page}.")
    except Exception as e:
        logging.error(f"Error processing '{input_file}': {e}")

def main():
    parser = argparse.ArgumentParser(description="Split PDF files into smaller PDFs.")
    parser.add_argument("--input-folder", "-i", type=str, default="./input", help="Folder containing input PDF files.")
    parser.add_argument("--output-folder", "-o", type=str, default="./output", help="Folder to save split PDF files.")
    parser.add_argument("--number-of-pages", "-n", type=int, default=1, help="Number of pages per split.")
    parser.add_argument("--prefix", "-p", type=str, default="", help="Custom prefix for output files.")
    parser.add_argument("--start-index", "-s", type=int, default=1, help="Start index for output file numbering.")
    parser.add_argument("--force", "-f", action="store_true", help="Overwrite existing files.")
    parser.add_argument("--clean", action="store_true", help="Clean output folder before processing.")
    parser.add_argument("--dry-run", action="store_true", help="Simulate actions without creating files.")
    parser.add_argument("--log-file", type=str, default="./logs/split_log.txt", help="Path to log file.")
    args = parser.parse_args()

    try:
        validate_arguments(args)
    except ValueError as e:
        logging.error(e)
        exit(1)

    setup_logging(args.log_file)

    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)
    elif args.clean:
        for file in os.listdir(args.output_folder):
            file_path = os.path.join(args.output_folder, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    logging.info(f"Deleted '{file_path}'.")
            except Exception as e:
                logging.error(f"Error deleting '{file_path}': {e}")

    pdf_files = [f for f in os.listdir(args.input_folder) if f.lower().endswith(".pdf")]
    if not pdf_files:
        logging.warning(f"No PDF files found in '{args.input_folder}'.")
        return

    for file_name in pdf_files:
        input_file = os.path.join(args.input_folder, file_name)
        split_pdf(input_file, args.output_folder, args.number_of_pages, args.prefix, args.start_index, args.dry_run, args.force)

if __name__ == "__main__":
    main()