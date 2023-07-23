<div align="center">

# Flet - ToastsFlexible

`ToastsFlexible`: is a control used the flet([website](https://flet.dev/), [github](https://github.com/flet-dev/flet)) python framework for push notifications to your visitors with a toast, a lightweight and easily customizable alert message.

<img src="media\ToastsFlexible.gif" width="65%"/>
</div>

## Features:
- **Customizable Toast Messages**: The can create toast messages with custom titles, descriptions, and icons. can tailor the appearance of the toast to match the specific needs of application.
- **Positioning Options**: Toast messages can be positioned at different corners or center of the screen, providing flexibility in where the messages appear.
- **Toast Actions**: The can add action buttons to the toast, allowing users to interact with the toast and perform specific actions when buttons are clicked.
- **Auto-Close**: Toasts can be set to automatically disappear after a specified duration, making it convenient for displaying temporary messages or notifications.
- **Progress Bar for Auto-Close**: When auto-closing is enabled, a progress bar is displayed to indicate the time remaining before the toast disappears.
- **Toast History**: The toasts supports maintaining a history of displayed toasts, including their timestamps, titles, descriptions, and time ago when each toast was displayed.
- **Integration with User Interface**: The toast can be easily integrated into an existing UI by passing a Page object during initialization.
- **Flexible Styling**: The can customize the appearance of the toast, including background colors, width, shadow, and alignment of elements.
- **Overlay**: The efficiently manages overlay controls to display toasts on top of the user interface.
- **Interval live time**: The include opening time of the toast. with time update.

*Overall, the ToastsFlexible class provides a powerful and customizable toast messaging system for applications, enabling developers to display informative and interactive messages in a user-friendly manner.*

## Examples & Usage
> Note: `ToastsFlexible` can be used as a with trigger click or without.

### 1- Toast with trigger and auto close.

<div align="center">
    <img src="media\Toast_with_trigger_and_auto_close.gif" width="55%"/>
</div>

```python
import flet as ft
from flet_contrib.toasts_flexible import ToastAction, ToastPosition, ToastsFlexible

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
```

### 2- Toast without trigger.

<div align="center">
    <img src="media\Toast_without_trigger.gif" width="55%"/>
</div>

```python
import flet as ft
from flet_contrib.toasts_flexible import ToastAction, ToastPosition, ToastsFlexible

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
            position=ToastPosition.TOP_RIGHT,
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
```

### 3- Toast with set interval random.

<div align="center">
    <img src="media\Toast_interval_random.gif" width="55%"/>
</div>

```python
import flet as ft
from flet_contrib.toasts_flexible import ToastAction, ToastPosition, ToastsFlexible

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
```

### 4- Toast title only and interval 1 second for update.

<div align="center">
    <img src="media\Toast_title_only_and_interval_second_update.gif" width="55%"/>
</div>

```python
import flet as ft
from flet_contrib.toasts_flexible import ToastAction, ToastPosition, ToastsFlexible

# DESC => Set dictionary empty to history of toasts.
toasts_history = {}

def main(page: ft.Page):
    # DESC => Toast title only and interval 1 second update.
    button = ft.ElevatedButton("Toast", 
        on_click=lambda _: ToastsFlexible(
            page=page,
            icon=ft.icons.INFO,
            title="Toast title only and interval",
            interval_random=False,
            interval_update=1,
            refresh_runs=10,
            position=ToastPosition.TOP_LEFT,
            set_history_desc=".....",
            set_history=toasts_history,
        )
    )

    page.add(button)
    page.update()

ft.app(target=main)
```

### 5- Toast description only and auto close.

<div align="center">
    <img src="media\Toast_description_only_and_auto_close.gif" width="55%"/>
</div>

```python
import flet as ft
from flet_contrib.toasts_flexible import ToastAction, ToastPosition, ToastsFlexible

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
```

### 6- Toast with description customized and hide title.

<div align="center">
    <img src="media\Toast_description_customized_without_title.gif" width="55%"/>
</div>

```python
import flet as ft
from flet_contrib.toasts_flexible import ToastAction, ToastPosition, ToastsFlexible

# DESC => Set dictionary empty to history of toasts.
toasts_history = {}

def main(page: ft.Page):
    # DESC => Toast with description customized and hide title.
    button = ft.ElevatedButton("Toast", 
        on_click=lambda _: ToastsFlexible(
            page=page,
            width=280,
            position=ToastPosition.BOTTOM_LEFT,
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
```

### 7- Toast with description customized and hide live time text.

<div align="center">
    <img src="media\Toast_description_customized_without_live_time.gif" width="55%"/>
</div>

```python
import flet as ft
from flet_contrib.toasts_flexible import ToastAction, ToastPosition, ToastsFlexible

# DESC => Set dictionary empty to history of toasts.
toasts_history = {}

def main(page: ft.Page):
    # DESC => Toast with description customized and hide live time text.
    button = ft.ElevatedButton("Toast", 
        on_click=lambda _: ToastsFlexible(
            page=page,
            width=220,
            title="New notification",
            position=ToastPosition.BOTTOM_RIGHT,
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
```

### -8 Output toast history.
```json
{
    "110b75b7-f79a-4690-a41d-41cf53cec69f": {
        "Toast without trigger": {
            "description": "Toast description", 
            "ago": {
                "Year": 2023, "Month": 7, "Day": 22, "Hour": 12, "Minute": 10, "Seconds": 41
            }
        }
    }, "a70df755-4bfa-445c-987f-de2368e43c79": {
        "Toast with trigger and auto close": {
            "description": "Toast description", 
            "ago": {
                "Year": 2023, "Month": 7, "Day": 22, "Hour": 12, "Minute": 10, "Seconds": 42
            }
        }
    }, "08244d9e-b937-4862-8810-ce5d9ee19e4d": {
        "Toast interval random": {
            "description": "Toast description", 
            "ago": {
                "Year": 2023, "Month": 7, "Day": 22, "Hour": 12, "Minute": 10, "Seconds": 42
            }
        }
    }, "700b8c18-72be-43a7-829d-185b3156a927": {
        "Toast title only and interval": {
            "description": ".....", 
            "ago": {
                "Year": 2023, "Month": 7, "Day": 22, "Hour": 12, "Minute": 10, "Seconds": 42
            }
        }
    }, "6f626d4c-06eb-4317-8bba-c9f2cafe835c": {
        ".....": {
            "description": "Toast description only and without interval but auto close", 
            "ago": {
                "Year": 2023, "Month": 7, "Day": 22, "Hour": 12, "Minute": 10, "Seconds": 43
            }
        }
    }, "595a0ca1-262e-434e-bc65-889c6b7fffc4": {
        "New notification": {
            "description": ".....", 
            "ago": {
                "Year": 2023, "Month": 7, "Day": 22, "Hour": 12, "Minute": 10, "Seconds": 43
            }
        }
    }, "66268d3d-2d4f-4fc0-b98c-497bb3c92fe1": {
        "Update available": {
            "description": ".....", 
            "ago": {
                "Year": 2023, "Month": 7, "Day": 22, "Hour": 12, "Minute": 10, "Seconds": 44
            }
        }
    }
}
```

## Properties ToastsFlexible
- `page` *(Page)*: The session start of the page container where the toast will be displayed. a for controls (widgets). It represents the user interface page where the toast will be shown.
- `icon` *(ft.icons, Optional)*: The icon to be displayed on the toast. It is an optional argument that allows users to customize the icon shown with the toast message. Defaults to None.
- `title` *(Union[str, Control], optional)*: The title of the toast message. It can be either a string or a Control object. If a Control object is used, the toast's title will be dynamic and update as per the control's value Defaults to None.
- `desc` *(Union[str, Control], optional)*: The description or main content of the toast message. It can be either a string or a Control object, enabling dynamic content display. Defaults to None.
- `bgcolor_title` *(ft.colors, optional)*: The background color of the toast title. This argument allows to customize the background color of the toast title section. Defaults to ft.colors.INVERSE_SURFACE.
- `bgcolor_desc` *(ft.colors, optional)*: The background color of the toast description. This argument allows to customize the background color of the toast description section. Defaults to ft.colors.ON_INVERSE_SURFACE.
- `shadow` *(Union[BoxShadow, List[BoxShadow]], optional)*: The shadow customization for the toast. can set the shadow properties, to add a shadow effect to the toast. Defaults to None.
- `no_live_time` *(bool)*: That determines whether to show live time text to the toast. If set to True, the toast will not display any time information. Defaults to False.
- `position` *(ToastPosition, optional)*: The position of the toast on the screen. It is an optional argument that allows to set the toast's position to one of the predefined positions, such as top-left etc. Defaults to ToastPosition.TOP_RIGHT.
- `actions` *(List[ToastAction], optional)*: A list of action buttons to be added to the toast. can provide a list of `ToastAction` objects to create interactive buttons within the toast. Defaults to None.
- `actions_alignment` *(MainAxisAlignment, optional)*: The alignment of the action buttons within the toast. It is an optional argument that allows to set the alignment of the buttons, such as start, end, or center.
- `auto_close` *(Union[int, float], optional)*: The time duration (in seconds) after which the toast will automatically close and disappear. If set to None, the toast will not auto-close. Defaults to None.
- `width` *(Union[int, float], optional)*: The width of the toast in pixels. If not provided. Defaults to 350.
- `trigger` *(Control, optional)*: An optional control that can be used to trigger the display of the toast. If a control with an `on_click` attribute is provided, the toast will be shown when the control is clicked. Defaults to None.
- `set_history_title` *(str, optional)*: An optional title to set for the toast's history entry. This argument is used if use a control in `"title"`, or want to set a specific title for the history entry. Defaults to None.
- `set_history_desc` *(str, optional)*: An optional description to set for the toast's history entry. This argument is used if use a control in `"desc"`, or want to set a specific description for the history entry. Defaults to None.
- `set_history` *(Dict, optional)*: A dictionary to store the history of displayed toasts. If provided, the dictionary will be updated with the timestamp, title, description, and time ago when each toast is displayed. Defaults to None.
- `interval_update` *(Union[int, float], optional)*: The time interval (in seconds) between each update of the opening time of the toast. If set, the opening time will be refreshed at the specified interval. Defaults to 5.
- `interval_random` *(bool, optional)*: A boolean flag that determines whether to set a random interval between each update. If set to True, the opening time will be refreshed at random intervals between updates. Defaults to False.
- `refresh_runs` *(Union[int, float], optional)*: The time interval (in seconds) for an refresh loop run. If provided, the opening time will be refreshed continuously at the specified interval until the toast is closed or auto-closes, if use None or set param `auto_close` or set `no_live_time` True you will not update. Defaults to None.

## Properties ToastAction
- `key` *(Any, optional)*: An optional key to uniquely identify the control. It can be used for custom indexing or identification purposes. Defaults to None.
- `data` *(Any, optional)*: An optional data value associated with the control. This data can be used to store additional information related to the control. Defaults to None.
- `text` *(str, optional)*: The text or label to be displayed on the control. It represents the visible text on the button. Defaults to None.
- `width` *(Union[int, float], optional)*: The width of the control in pixels. If not provided, the width will be automatically determined based on the content. Defaults to None.
- `height` *(Union[int, float], optional)*: The height of the control in pixels. If not provided. Defaults to 28.
- `url` *(str, optional)*: An optional URL to be opened when the control is clicked. If set, on_click event is fired after that. Defaults to None.
- `url_target` *(str, optional)*: An optional target attribute for the URL specified in url. It determines where the URL will be opened, such as "_blank" for a new tab or "_self" for the current tab. Defaults to None.
- `on_hover` *(Callable[[ControlEvent], None], optional)*: A callback function that will be triggered when the mouse pointer hovers over the control. Defaults to None.
- `on_click` *(Callable[[ControlEvent], None], optional)*: A callback function that will be triggered when the control is clicked. Defaults to None.
- `on_long_press` *(Callable[[ControlEvent], None], optional)*: A callback function that will be triggered when the control is long-pressed. Defaults to None.
- `disabled` *(bool, optional)*: A boolean flag that determines whether the control is disabled. If set to True, the control will be non-interactive. Defaults to None.
- `color` *(Union[None, str, Dict[Union[str, MaterialState], str]])*: The text color of the control. It can be specified as a color string or a dictionary containing mappings for different states `{"": "red", "hovered": "blue", ft.MaterialState.FOCUSED: ft.colors.WHITE}`. Defaults to None.
- `bgcolor` *(Union[None, str, Dict[Union[str, MaterialState], str]])*: The background color of the control. It can be specified as a color string or a dictionary containing mappings for different states `{"": "red", "hovered": "blue", ft.MaterialState.FOCUSED: ft.colors.WHITE}`. Defaults to None.
- `action_style` *(str, optional)*: The style of the button. It can be one of four options: `"elevated"`, `"filled"`, `"outlined"`, or `"texted"`. Defaults to "texted".

## Properties ToastPosition
Property value is ToastPosition enum with the following values:

- `TOP_CENTER`
- `TOP_LEFT`
- `TOP_RIGHT` (default)
- `BOTTOM_CENTER`
- `BOTTOM_LEFT`
- `BOTTOM_RIGHT`
- `CENTER`
- `CENTER_LEFT`
- `CENTER_RIGHT`