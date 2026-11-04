import flet as ft

def main(page: ft.Page):
    page.title = "Calcolatrice"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 500

    result = ft.Text(value="0", size=32, weight=ft.FontWeight.BOLD)

    def button_clicked(e):
        data = e.control.text
        if data == "C":
            result.value = "0"
        elif data == "=":
            try:
                result.value = str(eval(result.value))
            except Exception:
                result.value = "Errore"
        else:
            if result.value == "0" or result.value == "Errore":
                result.value = data
            else:
                result.value += data
        page.update()

    btn_rows = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"]
    ]

    controls = [result]
    for row in btn_rows:
        row_controls = [
            ft.ElevatedButton(text=btn, width=60, height=60, on_click=button_clicked)
            for btn in row
        ]
        controls.append(ft.Row(row_controls, alignment=ft.MainAxisAlignment.CENTER))

    page.add(
        ft.Column(
            controls,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )
