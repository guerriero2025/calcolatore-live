import flet as ft

def main(page: ft.Page):
    page.title = "Calcolatore Copertura Live (1-2 -> X)"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 10
    page.window_width = 380
    page.window_height = 650
    page.window_resizable = False

    # Campi di input
    stake_12 = ft.TextField(label="Puntata Iniziale 1-2 (€)", value="10", text_align=ft.TextAlign.RIGHT, keyboard_type=ft.KeyboardType.NUMBER)
    odds_12 = ft.TextField(label="Quota Doppia Chance 1-2", value="1.45", text_align=ft.TextAlign.RIGHT, keyboard_type=ft.KeyboardType.NUMBER)
    odds_x = ft.TextField(label="Quota Live X (Pareggio)", value="3.50", text_align=ft.TextAlign.RIGHT, keyboard_type=ft.KeyboardType.NUMBER)

    # Campi di output (Risultati)
    res_puntata_x = ft.Text("Puntata su X consigliata: --", weight=ft.FontWeight.BOLD, size=15, color=ft.colors.BLUE_700)
    res_utile_pareggio = ft.Text("Utile se esce X: --", size=13)
    res_utile_segno = ft.Text("Utile se vince 1 o 2: --", size=13)

    def calcola(e):
        try:
            s = float(stake_12.value.replace(',', '.'))
            o12 = float(odds_12.value.replace(',', '.'))
            ox = float(odds_x.value.replace(',', '.'))

            potenziale_vincita = s * o12
            puntata_x = potenziale_vincita / ox
            
            investimento_totale = s + puntata_x
            
            res_puntata_x.value = f"Puntata su X consigliata: {puntata_x:.2f} €"
            res_utile_pareggio.value = f"Incasso totale se esce X: {potenziale_vincita:.2f} € (Spesa tot: {investimento_totale:.2f} €)"
            res_utile_segno.value = f"Se vince 1 o 2 recuperi/gestisci la giocata"
            
            page.update()
        except ValueError:
            res_puntata_x.value = "Errore: inserisci numeri validi"
            page.update()

    btn_calcola = ft.ElevatedButton("Calcola Copertura Live", on_click=calcola, color=ft.colors.WHITE, bgcolor=ft.colors.GREEN_700, width=320)

    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("⚡ Copertura 1-2 vs X", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN_800),
                    ft.Divider(),
                    stake_12,
                    odds_12,
                    odds_x,
                    ft.Container(height=5),
                    btn_calcola,
                    ft.Divider(),
                    res_puntata_x,
                    res_utile_pareggio,
                ], tight=True, spacing=12),
                padding=15,
            )
        )
    )

ft.app(target=main)
