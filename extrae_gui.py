import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import messagebox

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

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, file_path)

def extract_specific_pages():
    input_pdf = input_file_entry.get()
    output_pdf = output_file_entry.get()
    pages = list(map(int, specific_pages_entry.get().split(',')))
    
    try:
        extract_pages(input_pdf, output_pdf, pages)
        messagebox.showinfo("Éxito", f"Las páginas {pages} han sido extraídas de {input_pdf} y guardadas en {output_pdf}.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def extract_range_of_pages():
    input_pdf = input_file_entry.get()
    output_pdf = output_file_entry.get()
    start_page = int(start_page_entry.get())
    end_page = int(end_page_entry.get())
    
    try:
        extract_page_range(input_pdf, output_pdf, start_page, end_page)
        messagebox.showinfo("Éxito", f"Las páginas desde la {start_page} hasta la {end_page} han sido extraídas de {input_pdf} y guardadas en {output_pdf}.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Función para mostrar el mensaje
def mostrar_mensaje():
    messagebox.showinfo("Sapere aude", "                   Manuel Álvaro Pacheco Hoyo\n                               Carpe diem\nAequam memento rebus in arduis servare mentem")


# Crear la ventana principal

root = tk.Tk()
root.title("Extractor de Páginas de PDF")

# Crear y colocar los widgets en la ventana
tk.Label(root, text="Archivo PDF de entrada:").grid(row=0, column=0, padx=10, pady=10)
input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Seleccionar archivo", command=select_input_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Archivo PDF de salida:").grid(row=1, column=0, padx=10, pady=10)
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Seleccionar archivo", command=select_output_file).grid(row=1, column=2, padx=10, pady=10)

tk.Label(root, text="Páginas específicas (separadas por comas):").grid(row=2, column=0, padx=10, pady=10)
specific_pages_entry = tk.Entry(root)
specific_pages_entry.grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Extraer páginas específicas", command=extract_specific_pages).grid(row=2, column=2, padx=10, pady=10)

tk.Label(root, text="Rango de páginas - Inicio:").grid(row=3, column=0, padx=10, pady=10)
start_page_entry = tk.Entry(root)
start_page_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Rango de páginas - Fin:").grid(row=4, column=0, padx=10, pady=10)
end_page_entry = tk.Entry(root)
end_page_entry.grid(row=4, column=1, padx=10, pady=10)

tk.Button(root, text="Extraer rango de páginas", command=extract_range_of_pages).grid(row=5, columnspan=3, padx=10, pady=20)

tk.Button(root, text="Acerca de:", command=mostrar_mensaje).grid(row=4, column=2, padx=30, pady=30)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
