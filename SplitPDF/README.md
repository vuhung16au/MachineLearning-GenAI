# Introduction

# How to Setup 

Install Python first

```bash
python3 -m venv .venv
```

On Mac OS
```
source .venv/bin/activate
```

On Windows 
```
cd C:\Users\YourUsername\YourProject
.venv\Scripts\Activate.ps1
```

Install dependencies:
```
(.venv) $ pip install -r requirements.txt
```

# How to Run

- Put pdf to be splitted into folder `input`
- Run `SplitPDF.py`
- Splitted pdf files will be saved under folder `output`

# An Use Case 

Payslips for 60 staffs reveived from external company is a 60-page and each payslip for each staff is in one page.
We want to split the file to 60 small, each page in a file after splitting.