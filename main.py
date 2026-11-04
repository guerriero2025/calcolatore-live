import flet as ft

def main(page: ft.Page):
    try:
        page.title = "Calcolatrice"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # Display del risultato
        display = ft.Text(value="0", size=36, weight=ft.FontWeight.BOLD)

        def button_clicked(e):
            data = e.control.text
            if data == "C":
                display.value = "0"
            elif data == "=":
                try:
                    display.value = str(eval(display.value))
                except Exception:
                    display.value = "Errore"
            else:
                if display.value == "0" or display.value == "Errore":
                    display.value = data
                else:
                    display.value += data
            page.update()

        # Aggiungiamo il display alla pagina
        page.add(display)

        # Griglia dei pulsanti
        btn_rows = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]

        for row in btn_rows:
            row_controls = [
                ft.ElevatedButton(text=btn, width=65, height=65, on_click=button_clicked)
                for btn in row
            ]
            page.add(ft.Row(row_controls, alignment=ft.MainAxisAlignment.CENTER, spacing=10))

    except Exception as ex:
        # Se si verifica un errore all'avvio, lo mostra sullo schermo anziché crashare
        page.add(ft.Text(f"Errore: {ex}", size=20, color="red"))

    page.update()
