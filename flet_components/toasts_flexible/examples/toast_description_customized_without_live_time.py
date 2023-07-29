import flet as ft
from flet_components.toasts_flexible import ToastAction, ToastsFlexible
from flet_components.core import Position

# DESC => Set dictionary empty to history of toasts.
toasts_history = {}

def main(page: ft.Page):
    # DESC => Toast with description customized and hide live time text.
    button = ft.ElevatedButton("Toast", 
        on_click=lambda _: ToastsFlexible(
            page=page,
            width=220,
            title="New notification",
            position=Position.BOTTOM_RIGHT,
            no_live_time=True,
            set_history_desc=".....",
            set_history=toasts_history,
            desc=ft.Row(
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12,
                controls=[
                    ft.Stack(
                        width=50,
                        height=50,
                        controls=[
                            ft.CircleAvatar(
                                radius=50,
                                foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4"
                            ),

                            ft.Container(
                                content=ft.CircleAvatar(
                                    radius=11.5,
                                    color=ft.colors.PRIMARY,
                                    bgcolor=ft.colors.ON_PRIMARY,
                                    content=ft.Icon(ft.icons.CHAT, size=15),
                                ),
                                alignment=ft.alignment.bottom_right,
                            ),
                        ]
                    ),
                    
                    ft.Column(
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        spacing=1,
                        controls=[
                            ft.Text("Toast Flexible", style=ft.TextThemeStyle.BODY_MEDIUM, weight=ft.FontWeight.BOLD),
                            ft.Text("commmented on your photo", style=ft.TextThemeStyle.BODY_SMALL),
                            ft.Text("a few seconds ago", style=ft.TextThemeStyle.LABEL_SMALL, color=ft.colors.PRIMARY),
                        ]
                    ),
                ]
            ),
        )
    )

    page.add(button)
    page.update()

ft.app(target=main)
