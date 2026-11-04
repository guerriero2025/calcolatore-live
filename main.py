import flet as ft

def main(page: ft.Page):
    page.title = "Calcolatrice"
    page.padding = 20
    page.window.width = 350
    page.window.height = 550

    result = ft.Text(
        value="0", size=36, weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.RIGHT, expand=True, no_wrap=True
    )
    
    display = ft.Container(
        content=result, bgcolor="#f0f0f0", padding=20,
        border_radius=10, expand=True, alignment=ft.alignment.center_right
    )

    def button_clicked(e):
        data = e.control.text
        if data == "C":
            result.value = "0"
        elif data == "⌫":
            result.value = result.value[:-1] if len(result.value) > 1 else "0"
        elif data == "=":
            try:
                result.value = str(eval(result.value))
            except Exception:
                result.value = "Errore"
        else:
            if result.value in ("0", "Errore"):
                result.value = data
            else:
                result.value += data
        page.update()

    btn_rows = [
        ["C", "⌫", "/", "*"],
        ["7", "8", "9", "-"],
        ["4", "5", "6", "+"],
        ["1", "2", "3", "="],
        ["0", ".", "", ""]
    ]

    controls = [display]
    for row in btn_rows:
        row_controls = [
            ft.ElevatedButton(text=btn, expand=True, height=60, on_click=button_clicked)
            for btn in row if btn != ""
        ]
        controls.append(ft.Row(row_controls, spacing=10, expand=True))

    page.add(ft.Column(controls, spacing=10, expand=True))

if __name__ == "__main__":
    ft.app(target=main)
