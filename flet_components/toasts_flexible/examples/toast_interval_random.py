import flet as ft
from flet_components.toasts_flexible import ToastAction, ToastPosition, ToastsFlexible

# DESC => Set dictionary empty to history of toasts.
toasts_history = {}

def main(page: ft.Page):
    # DESC => Toast with set interval random.
    button = ft.ElevatedButton("Toast", 
        on_click=lambda _: ToastsFlexible(
            page=page,
            icon=ft.icons.INFO,
            title="Toast interval random",
            desc="Toast description",
            interval_random=True,
            interval_update=None,
            refresh_runs=10,
            position=ToastPosition.TOP_LEFT,
            set_history=toasts_history,
        )
    )

    page.add(button)
    page.update()

ft.app(target=main)
