# AUTOMATED-REPORT-GENERATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KALYAM CHANDU REDDY

*INTERN ID*: CTIS6413

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 12 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR

 Automated Report Generation

This project implements a **dynamic automated reporting system** using Python that reads different file formats, performs analysis, and generates a **structured PDF report**. The goal was to demonstrate **file handling, data processing, and automated report generation** in a real-world scenario.

---

### 🔧 Project Implementation

The system was developed in **Python using Visual Studio Code**, leveraging:

* `pandas` for data analysis
* `fpdf` for PDF report generation
* `os` and `datetime` for file handling and timestamps

The script accepts a **user-provided file path**, making it flexible and reusable for multiple file types.

---

### ⚙️ Working Flow

```text
Input File → Type Detection → Data Analysis → PDF Report Generation
```

The system automatically detects the file type and processes it accordingly:

* **CSV / Excel Files**

  * Extracts rows, columns, and column names
  * Identifies missing values
  * Computes statistics (mean, min, max for numeric data)

* **Text Files (.txt)**

  * Calculates total lines, words, and characters

---

### 📑 Output Report

A clean and formatted PDF report is generated containing:

* Report title and timestamp
* File name details
* Structured analysis results

The report is saved as:

```
Automated_Analysis_Report.pdf
```

---

### 💡 Key Highlights

* Supports multiple formats: `.csv`, `.xlsx`, `.txt`
* Fully dynamic input system
* Modular and clean code design
* Automatic PDF generation with structured formatting
* Error handling for invalid or unsupported files

---

### 🚀 Use Cases

* Automated data reporting
* Business analytics summaries
* File inspection tools
* Data preprocessing pipelines

---

### 📌 Conclusion

This project demonstrates how Python can automate the process of **reading, analyzing, and converting data into meaningful reports**, making it a practical solution for real-world data workflows.

### 📌 Output

<img width="798" height="770" alt="Image" src="https://github.com/user-attachments/assets/aebb3a19-b37e-4d7f-8643-80d4dce7ff09" />
