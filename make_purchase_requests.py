from pypdf import PdfReader, PdfWriter
from csv import DictReader
from argparse import ArgumentParser
import os
import logging

tax_rate = 0.0725

def make_purchase_requests(input_file: str, template_file: str, lines_per: int = 15):
    filename_no_ext = os.path.basename(input_file.replace('\\', '/')).split('.')[0]
    blank_pdf = PdfReader(template_file)

    shipping = float(input('Enter the shipping cost: '))

    logging.debug(f'Input file: {input_file}')
    logging.debug(f'Filename no ext: {filename_no_ext}')

    with open(input_file, 'r') as file:
        input_csv = list(DictReader(file))

    logging.info(f'Processing {len(input_csv)} line items')

    purchase_order_splits = [input_csv[i:i+lines_per] for i in range(0, len(input_csv), lines_per)]

    logging.info(f'Creating {len(purchase_order_splits)} purchase orders')

    for i, purchase_order in enumerate(purchase_order_splits):
        output_pdf = PdfWriter()

        output_pdf.append(blank_pdf)

        sum = 0

        for j, line_item in enumerate(purchase_order):
            logging.debug(f'Adding line item: {line_item}')

            line_no = i * lines_per + j + 1

            output_pdf.update_page_form_field_values(output_pdf.pages[0], {
                f'Line ItemRow{j+1}': line_no,
                f'Catalog Row{j+1}': line_item['Catalog#'],
                f'QTYRow{j+1}': line_item['Qty'],
                f'Item DescriptionRow{j+1}': line_item['ItemDescription'],
                f'Haz Mat YNRow{j+1}': line_item['HazMat'],
                f'Unit PriceRow{j+1}': line_item['UnitPrice'],
                f'Amt Row {j+1}': f"{float(line_item['Qty']) * float(line_item['UnitPrice']):.2f}",
            }, auto_regenerate=True)

            sum += float(line_item['Qty']) * float(line_item['UnitPrice'])

        this_item_shipping = shipping if i == len(purchase_order_splits) - 1 else 0

        output_pdf.update_page_form_field_values(output_pdf.pages[0], {
            'Est Total': f"{sum:.2f}",
            'Est Tax': f"{(sum * tax_rate):.2f}",
            'Est Shipping': f"{this_item_shipping:.2f}",
            'Act Total': f"{(sum * (1.0 + tax_rate) + this_item_shipping):.2f}",
        }, auto_regenerate=True)

        output_pdf.write(f'{filename_no_ext}_{i+1}.pdf')

def main():
    parser = ArgumentParser(description='Make purchase requests from a CSV file')
    parser.add_argument('input_file', help='The input CSV file')
    parser.add_argument('template_file', help='The template PDF file')
    parser.add_argument('--lines', help='The number of lines per purchase request', type=int, default=15)
    parser.add_argument('--quiet', action='store_true', help='Suppress logging output')
    parser.add_argument('--verbose', action='store_true', help='Print verbose logging output')
    parser.add_argument('--debug', action='store_true', help='Print debug logging output')
    args = parser.parse_args()

    if args.quiet:
        logging.basicConfig(level=logging.ERROR)
    elif args.verbose:
        logging.basicConfig(level=logging.INFO)
    elif args.debug:
        logging.basicConfig(level=logging.DEBUG)

    logging.debug(f'Arguments: {args}')

    make_purchase_requests(args.input_file, args.template_file, args.lines)

if __name__ == '__main__':
    main()