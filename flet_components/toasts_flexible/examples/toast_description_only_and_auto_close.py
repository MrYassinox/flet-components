import flet as ft
from flet_components.toasts_flexible import ToastAction, ToastPosition, ToastsFlexible

# DESC => Set dictionary empty to history of toasts.
toasts_history = {}

def main(page: ft.Page):
    # DESC => Toast description only and auto close.
    button = ft.ElevatedButton("Toast", 
        on_click=lambda _: ToastsFlexible(
            page=page,
            desc="Toast description only and auto close.",
            auto_close=5,
            position=ToastPosition.TOP_LEFT,
            set_history_title=".....",
            set_history=toasts_history,
        )
    )

    page.add(button)
    page.update()

ft.app(target=main)
