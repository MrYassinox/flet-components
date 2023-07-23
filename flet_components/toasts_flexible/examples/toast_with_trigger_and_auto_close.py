import flet as ft
from flet_components.toasts_flexible import ToastAction, ToastPosition, ToastsFlexible

# DESC => Set dictionary empty to history of toasts.
toasts_history = {}

def main(page: ft.Page):
    # DESC => Toast with trigger and auto close.
    button = ft.ElevatedButton("Toast")

    ToastsFlexible(
        page=page,
        icon=ft.icons.INFO,
        title="Toast with trigger and auto close",
        desc="Toast description",
        position=ToastPosition.TOP_RIGHT,
        auto_close=5,
        set_history=toasts_history,
        trigger=button
    )

    page.add(button)
    page.update()

ft.app(target=main)
