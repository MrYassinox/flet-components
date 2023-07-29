import flet as ft
from flet_components.toasts_flexible import ToastAction, ToastsFlexible
from flet_components.core import Position

# DESC => Set dictionary empty to history of toasts.
toasts_history = {}

def main(page: ft.Page):
    # DESC => Toast with description customized and hide title.
    button = ft.ElevatedButton("Toast", 
        on_click=lambda _: ToastsFlexible(
            page=page,
            width=280,
            position=Position.BOTTOM_LEFT,
            no_live_time=True,
            set_history_title="Update available",
            set_history_desc=None,
            set_history=toasts_history,
            desc=ft.Row(
                expand=True,
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.START,
                spacing=12,
                controls=[
                    ft.Icon(ft.icons.UPDATE, size=24),

                    ft.Column(
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        spacing=0,
                        controls=[
                            ft.Text("Update available", 
                                style=ft.TextThemeStyle.BODY_MEDIUM, 
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text("A new software version is available for download.", 
                                style=ft.TextThemeStyle.LABEL_MEDIUM, 
                                width=210,
                                opacity=0.8
                            ),
                        ]
                    ),
                ]
            ),
            actions_alignment=ft.MainAxisAlignment.CENTER,
            actions=[
                ToastAction(
                    text="Update",
                    width=100,
                    action_style="filled",
                    disabled=False,
                    on_click=lambda e: print(toasts_history),
                ),
                ToastAction(
                    text="Not update",
                    width=100,
                    action_style="outlined",
                    disabled=False,
                    on_click=lambda e: print(toasts_history),
                )
            ]
        )
    )

    page.add(button)
    page.update()

ft.app(target=main)
