# IRA Purchase Request Automator
Hello, wayward traveler!If you've somehow stumbled upon this in your random travels of the internet,
this repository is completely useless to you! Move along and happy travels :D

If you're an officer of a student organization at Cal State LA which receives
funding from the Department of ECST under IRA allocations, welcome! If somehow
you fit that bill **AND** randomly stumbled upon this repository... how?

## Preface
Anyone who's filled out an IRA purchase request  form knows how much of a
hassle it can be, as copying every product number, quantity and cost,
description and whatnot to multiple different PDFs for sending off is a
tedious task, and one it's suprising hasn't been streamlined before. Why
must we subject ourselves to the pain of such a task, when the very wonders
of computer science are at our fingertips? Let me blow your mind and
introduce you to the tool I've created to ease our lives a little bit.

## Requirements
- Know how to use a terminal (Command Prompt, PowerShell, Bash, etc.)
- Install [Python](https://www.python.org/downloads/)
- Install pypdf (`pip install pypdf` from a terminal)
- Download the [IRA Purchase Request Form](https://www.calstatela.edu/sites/default/files/ira_purchase_request_form_rev_8_22.pdf)

## Usage
As you (hopefully) know, a separate IRA purchase form must be submitted for
every vendor you want to buy from. So to start, fill out the request form
only as far as your team name, the vendor name/contact info, and
requestor/advisor name and contact. Leave the item table blank! That's the
magic of this tool. Do this once for every vendor your team uses/plans to
use, and save each partially-filled PDF under a memorable name. I often use
`BLANK_<vendor>-ira-pr.pdf` as my filenames. These part-filled PDFs will
henceforth be called our "template files", as they will be automatically
populated to make our purchase requests.

For every purchase request you wish to make, you should then create a CSV
file of all items you want to purchase. An example of a properly formatted
file is included with this script as `example_pr_csv.csv`. The easiest way to
do this is to make a spreadsheet in a tool like Google Sheets or Microsoft
Excel and then export the sheet to a CSV file. It is important to include the
correct header no matter which software you use, so an example file for
Google Sheets can be found [here](https://docs.google.com/spreadsheets/d/1C_caJ13kP4k8Shic1FmBr4MGKgDgp2dFIQGbyo4OsA0/edit?usp=sharing).
Further items should be added as additional rows. Do not delete the header
(row 1). Your sheet can then be exported as a CSV using your software's
specific context menus. For Google Sheets, this is under File->Download.

You're now ready to use the tool! Open a terminal and navigate to the
directory you've cloned it into. Take note of the path to your previously
created template file and downloaded purchase request CSV file. Run the tool
with the following syntax:

Windows: `python .\make_purchase_requests.py <path_to_template> <path_to_csv>`  
Linux: `python3 .\make_purchase_requests.py <path_to_template> <path_to_csv>`

Your purchase request PDFs should be ready! They will be generated with a
filename based on the date, vendor name, and then sequentially if multiple
files must be generated. Sign, send, and enjoy!