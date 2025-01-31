import fitz  # PyMuPDF

def extract_pages(input_pdf, output_pdf, pages):
    # Abrir el PDF de entrada
    pdf_document = fitz.open(input_pdf)
    
    # Crear un nuevo PDF para las páginas extraídas
    new_pdf = fitz.open()
    
    # Extraer las páginas especificadas
    for page_num in pages:
        new_pdf.insert_pdf(pdf_document, from_page=page_num-1, to_page=page_num-1)
    
    # Guardar el nuevo PDF
    new_pdf.save(output_pdf)
    new_pdf.close()
    pdf_document.close()

def extract_page_range(input_pdf, output_pdf, start_page, end_page):
    # Abrir el PDF de entrada
    pdf_document = fitz.open(input_pdf)
    
    # Crear un nuevo PDF para las páginas extraídas
    new_pdf = fitz.open()
    
    # Extraer el rango de páginas especificado
    new_pdf.insert_pdf(pdf_document, from_page=start_page-1, to_page=end_page-1)
    
    # Guardar el nuevo PDF
    new_pdf.save(output_pdf)
    new_pdf.close()
    pdf_document.close()

# Ejemplo de uso para extraer páginas específicas
input_pdf = "FAO_1995_ECP-2.pdf"
output_pdf = "output_specific_pages.pdf"
pages_to_extract = [1, 3, 5]  # Páginas a extraer (1-indexadas)

extract_pages(input_pdf, output_pdf, pages_to_extract)
print(f"Las páginas {pages_to_extract} han sido extraídas de {input_pdf} y guardadas en {output_pdf}.")

# Ejemplo de uso para extraer un rango de páginas
output_pdf_range = "CYNOGLOSSIDAE.pdf"
start_page = 401
end_page = 421

extract_page_range(input_pdf, output_pdf_range, start_page, end_page)
print(f"Las páginas desde la {start_page} hasta la {end_page} han sido extraídas de {input_pdf} y guardadas en {output_pdf_range}.")


