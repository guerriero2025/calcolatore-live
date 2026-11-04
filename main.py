import flet as ft

def main(page: ft.Page):
    page.title = "Test"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Solo una semplice scritta per verificare se l'app si avvia
    page.add(ft.Text("L'app funziona!", size=30))
