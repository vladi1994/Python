class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, 'r') as file:
            content = file.read()
        return content

    def write_file(self, content):
        with open(self.filename, 'w') as file:
            file.write(content)


class TextProcessor:
    @staticmethod
    def process_text(text):
        words = text.split()
        word_count = len(words)
        return word_count


def main():
    filename = 'example.txt'
    file_manager = FileManager(filename)
    text = file_manager.read_file()

    word_count = TextProcessor.process_text(text)
    print(f"Word count: {word_count}")

    new_text = "This is a new sentence."
    file_manager.write_file(new_text)
    print("New sentence written to file.")

if __name__ == "__main__":
    main()

# Explicación del código:

# FileManager: Esta clase se encarga de manejar la lectura y escritura de archivos. 
# Tiene dos métodos, read_file para leer el contenido de un archivo y write_file para escribir contenido en un archivo.

# TextProcessor: Esta clase se encarga de procesar el texto. 
# Tiene un método estático process_text que toma un texto y devuelve el número de palabras en él.

# main(): En la función principal, creamos una instancia de FileManager para manejar el archivo "example.txt". 
# Leemos el contenido del archivo, luego usamos la clase TextProcessor para contar las palabras en el texto y lo imprimimos. 
# Luego, escribimos una nueva oración en el archivo.

# Este ejemplo ilustra cómo las clases FileManager y TextProcessor tienen responsabilidades separadas y no se mezclan. 
# FileManager se encarga de las operaciones de archivos, mientras que TextProcessor se encarga del procesamiento de texto. 
# Esto sigue el principio de responsabilidad única, lo que hace que el código sea más modular y mantenible.