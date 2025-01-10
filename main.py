import pyray as rl

def main():
    book_path = "Nomina 1.2 con Deducciones.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)

    # Generar el reporte
    letter_dict = count_letter(text)
    sorted_dict = sorted(letter_dict.items(), key=lambda x: x[1], reverse=True)

    # Configuración de la ventana
    window_width, window_height = 800, 600
    rl.init_window(window_width, window_height, "Book Report Viewer")
    rl.set_target_fps(60)

    # Configuración del diseño
    font_size = 20
    margin = 20
    column_width = 100
    header_height = 40
    row_height = 30

    scroll_y = 0
    content_height = len(sorted_dict) * row_height + header_height

    animation_progress = 0  # Control de animación

    while not rl.window_should_close():
        # Movimiento del scroll
        if rl.is_key_down(rl.KEY_DOWN):
            scroll_y -= 5
        if rl.is_key_down(rl.KEY_UP):
            scroll_y += 5
        scroll_y = max(min(scroll_y, 0), -max(0, content_height - window_height + margin * 2))

        # Dibujar la pantalla
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)

        # Dibujar encabezados
        rl.draw_rectangle(margin, margin + scroll_y, window_width - 2 * margin, header_height, rl.DARKGRAY)
        rl.draw_text("Letter", margin + 10, margin + 10 + scroll_y, font_size, rl.RAYWHITE)
        rl.draw_text("Count", margin + column_width + 10, margin + 10 + scroll_y, font_size, rl.RAYWHITE)

        # Dibujar las filas
        y_offset = margin + header_height + scroll_y
        for idx, (letter, count) in enumerate(sorted_dict):
            # Alternar colores de fila
            if idx % 2 == 0:
                rl.draw_rectangle(margin, y_offset, window_width - 2 * margin, row_height, rl.LIGHTGRAY)

            # Dibujar datos de la fila
            rl.draw_text(letter, margin + 10, y_offset + 5, font_size, rl.DARKBLUE)
            if animation_progress >= idx:
                rl.draw_text(str(count), margin + column_width + 10, y_offset + 5, font_size, rl.DARKBLUE)
            y_offset += row_height

        # Incrementar animación
        animation_progress += 0.1

        rl.end_drawing()

    rl.close_window()

# Funciones auxiliares
def count_letter(text):
    letter_dic = {}
    for letter in text.lower():
        if letter.isalpha():
            letter_dic[letter] = letter_dic.get(letter, 0) + 1
    return letter_dic

def get_book_text(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return ""

def count_words(string):
    return len(string.split())

# Ejecutar el programa
if __name__ == "__main__":
    main()

