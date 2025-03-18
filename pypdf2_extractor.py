import os
import PyPDF2

def remove_second_page(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            with open(input_path, "rb") as infile:
                reader = PyPDF2.PdfReader(infile)
                writer = PyPDF2.PdfWriter()
                
                for i in range(len(reader.pages)):
                    if i != 1:  # Omitimos la segunda página (índice 1)
                        writer.add_page(reader.pages[i])
                
                with open(output_path, "wb") as outfile:
                    writer.write(outfile)
            
            print(f"Procesado: {filename}")

input_folder = "pdfs_entrada"  # Carpeta con los PDFs originales
output_folder = "pdfs_salida"  # Carpeta donde se guardarán los PDFs modificados

remove_second_page(input_folder, output_folder)
