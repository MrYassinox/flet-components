import flet as ft
from flet_components.toasts_flexible import ToastAction, ToastsFlexible
from flet_components.core import Position

# DESC => Set dictionary empty to history of toasts.
toasts_history = {}

def main(page: ft.Page):
    # DESC => Toast without trigger.
    button = ft.ElevatedButton("Toast", 
        on_click=lambda _: ToastsFlexible(
            page=page,
            icon=ft.icons.INFO,
            title="Toast without trigger",
            desc="Toast description",
            auto_close=None,
            trigger=None,
            set_history=toasts_history,
            position=Position.TOP_RIGHT,
            actions=[
                ToastAction(
                    text="action",
                    action_style="texted",
                    on_click=lambda e: print(toasts_history),
                )
            ]
        )
    )

    page.add(button)
    page.update()

ft.app(target=main)
