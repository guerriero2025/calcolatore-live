import flet as ft

def main(page: ft.Page):
    page.title = "Calcolatore"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    display_text = ft.Text(value="0", size=40, weight=ft.FontWeight.BOLD)

    def button_clicked(e):
        display_text.value = f"Premuto: {e.control.text}"
        page.update()

    page.add(
        ft.Column(
            [
                display_text,
                ft.Row(
                    [
                        ft.ElevatedButton(text="1", on_click=button_clicked),
                        ft.ElevatedButton(text="2", on_click=button_clicked),
                        ft.ElevatedButton(text="3", on_click=button_clicked),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
