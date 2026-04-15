import pandas as pd
from fpdf import FPDF
import os
from datetime import datetime


def analyze_tabular_data(df):
    """Analyzes CSV or Excel files and returns key metrics."""

    analysis = {
        "Type": "Tabular Data (CSV/Excel)",
        "Total Rows": len(df),
        "Total Columns": len(df.columns),
        "Columns": ", ".join(df.columns.tolist()),
        "Missing Values": int(df.isnull().sum().sum()),
    }

    numeric_cols = df.select_dtypes(include='number').columns

    if not numeric_cols.empty:

        analysis["Numeric Columns Found"] = len(numeric_cols)

        first_num_col = numeric_cols[0]

        analysis[f"Mean of '{first_num_col}'"] = round(df[first_num_col].mean(), 2)
        analysis[f"Min of '{first_num_col}'"] = round(df[first_num_col].min(), 2)
        analysis[f"Max of '{first_num_col}'"] = round(df[first_num_col].max(), 2)

    return analysis


def analyze_text_data(filepath):
    """Analyzes a plain text file and returns word/line counts."""

    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()

    lines = text.split('\n')
    words = text.split()

    analysis = {
        "Type": "Plain Text (.txt)",
        "Total Lines": len(lines),
        "Total Words": len(words),
        "Total Characters": len(text)
    }

    return analysis


def process_file(filepath):
    """Determines file type, reads it, and routes it to the correct analyzer."""

    if not os.path.exists(filepath):
        return None, "Error: File not found."

    file_ext = os.path.splitext(filepath)[1].lower()

    try:

        if file_ext == '.csv':

            df = pd.read_csv(filepath)
            return analyze_tabular_data(df), None

        elif file_ext in ['.xls', '.xlsx']:

            df = pd.read_excel(filepath)
            return analyze_tabular_data(df), None

        elif file_ext == '.txt':

            return analyze_text_data(filepath), None

        else:

            return None, f"Error: Unsupported file type '{file_ext}'. Please provide a .csv, .xlsx, or .txt file."

    except Exception as e:

        return None, f"An error occurred while reading the file: {str(e)}"


def generate_pdf_report(filename, analysis_data, output_pdf="Automated_Analysis_Report.pdf"):
    """Formats the analysis results into a PDF report."""

    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Automated Data Analysis Report", ln=True, align='C')

    pdf.ln(5)

    # Report date
    pdf.set_font("Arial", size=11)
    pdf.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)

    pdf.ln(3)

    # File info
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, f"Analyzed File: {os.path.basename(filename)}", ln=True)

    pdf.ln(5)

    # Section title
    pdf.set_font("Arial", 'B', 13)
    pdf.cell(0, 10, "Analysis Results", ln=True)

    pdf.ln(3)

    # Metrics
    pdf.set_font("Arial", size=12)

    for key, value in analysis_data.items():

        text_line = f"{key}: {value}"
        pdf.multi_cell(0, 8, text_line)

    pdf.ln(8)

    # Footer
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(0, 10, "Report generated automatically by Python Data Analyzer.", ln=True)

    pdf.output(output_pdf)

    print(f"\nSuccess! PDF Report generated: {output_pdf}")


def main():

    print("=== Automated File Analyzer ===")
    print("Supported formats: .csv, .xlsx, .txt")

    filepath = input("Enter the full path to the file you want to analyze: ").strip()

    if filepath.startswith('"') and filepath.endswith('"'):
        filepath = filepath[1:-1]

    print(f"\nProcessing '{filepath}'...")

    analysis_data, error = process_file(filepath)

    if error:
        print(error)

    else:
        generate_pdf_report(filepath, analysis_data)


if __name__ == "__main__":
    main()