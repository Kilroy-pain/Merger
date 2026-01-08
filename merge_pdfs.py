from pypdf import PdfWriter
import os

# List of files to merge in the desired order
files_to_merge = [
    "DBMS 01 INTRODUCTION TO DBMS pr.pdf",
    "DBMS 02 ENTITY RELATIONSHIP MODELLING pr.pdf",
    "DBMS 03 LIFECYCLE pr (1).pdf",
    "DBMS 04 NORMALIZATION.pdf",
    "DBMS 05 TRANSACTION AND CONCURRENCY CONTROL pr.pdf",
    "DBMS 07 SECURITY, INTEGRITY AND CONTROL pr.pdf",
    "SQL 1 pr.pdf",
    "SQL 2 pr.pdf"
]

def merge_pdfs(file_list, output_name):
    merger = PdfWriter()
    
    print("Starting merge process...")
    
    for filename in file_list:
        if os.path.exists(filename):
            print(f"Adding: {filename}")
            merger.append(filename)
        else:
            print(f"Warning: File not found - {filename}")
            
    merger.write(output_name)
    merger.close()
    print(f"Successfully created: {output_name}")

if __name__ == "__main__":
    merge_pdfs(files_to_merge, "Database Systems.pdf")
