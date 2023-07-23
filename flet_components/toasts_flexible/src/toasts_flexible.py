########################################################################################################################
# TODO DOCUMENT
########################################################################################################################
# |   ├──  |
# |   |    └── src: 
########################################################################################################################
# TODO IMPORTING NECESSARY LIBRARYIES
########################################################################################################################
# LIB python libraryies
import time
import random
from datetime import datetime
from typing import List, Any, Dict, Set, Callable, Union, Tuple, Iterable, Literal, Optional

# LIB => squardot-utils-standard libraryies
from utils_standard.modules.utils import time_sleep_accuracy, GenerateID

# LIB => flet libraryies
import flet as ft
from flet import UserControl, Control, Page
from flet_core import ControlEvent, ContainerTapEvent
from flet_core.shadow import BoxShadow
from flet_core.types import MainAxisAlignment, MaterialState

# LIB => from libraryies
from flet_components.core import OverlayPageManger, SetPosition, set_color_balance

########################################################################################################################
# TODO SET UP
########################################################################################################################
class ButtonIcon(UserControl):
    """ButtonIcon - Extended from UserControl class."""
    def __init__(self, 
        key: str = None,
        icon: ft.icons = None, 
        size: Union[int, float, None] = 22, 
        color: ft.colors = None, 
        bgcolor: ft.colors = None, 
        tooltip: str = None, 
        opacity: Union[int, float, None] = None, 
        visible: bool = None, 
        disabled: bool = None, 
        hovercolor: ft.colors = ft.colors.ON_SURFACE, 
        hover_duration: Union[int, None] = None,
        no_hover: bool = False,
        on_click: Callable[[ControlEvent], None] = None
        ): # DESC => initialize constructor.
        """Initialize the ButtonIcon object.

        Args:
            `key` (str, optional): _description_. Defaults to None.
            `icon` (ft.icons, optional): _description_. Defaults to None.
            `size` (Union[int, float, None], optional): _description_. Defaults to 22.
            `color` (ft.colors, optional): _description_. Defaults to None.
            `bgcolor` (ft.colors, optional): _description_. Defaults to None.
            `tooltip` (str, optional): _description_. Defaults to None.
            `opacity` (Union[int, float, None], optional): _description_. Defaults to None.
            `visible` (bool, optional): _description_. Defaults to None.
            `disabled` (bool, optional): _description_. Defaults to None.
            `hovercolor` (ft.colors, optional): _description_. Defaults to None.
            `hover_duration` (Union[int, None], optional): _description_. Defaults to None.
            `no_hover` (bool, optional): _description_. Defaults to False.
            `on_click` (Callable[[ControlEvent], None], optional): represent any callable object,
                such as a function, a method, or a lambda expression. Defaults to None.
        """
        super().__init__()
        # DESC => Initialize the state variables attribute.
        self._key = key
        self._icon = icon
        self._size = size
        self._color = color
        self._bgcolor = bgcolor
        self._tooltip = tooltip
        self._opacity = opacity
        self._visible = visible
        self._disabled = disabled
        self._hovercolor = hovercolor
        self._hover_duration = hover_duration
        self._no_hover = no_hover
        self._on_click = on_click

    def on_button_hover_event(self, event: ContainerTapEvent):
        """Is a callable object, such as a function a method or a lambda expression.
        The Callable function that takes an argument of type event"""
        if self._no_hover:
            if event.control.content.opacity != 1:
                event.control.content.opacity = 1
            else:
                event.control.content.opacity = 0.5
        else:
            if event.control.bgcolor != ft.colors.with_opacity(opacity=0.08, color=self._hovercolor):
                event.control.bgcolor = ft.colors.with_opacity(opacity=0.08, color=self._hovercolor)
            else:
                event.control.bgcolor = None
        event.control.update()

    def build(self):
        """The initialize build control's UI."""
        self._size = self._size if self._size else 22
        self.padding = 0 if self._no_hover else 5
        self.size_final = (self.padding + self._size) if self._no_hover else (self.padding + self._size + 10)

        self.builder = ft.Stack(
            width=self.size_final,
            height=self.size_final,
            opacity=self._opacity,
            visible=self._visible,
            disabled=self._disabled,
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    bgcolor=self._bgcolor,
                    padding=ft.padding.all(self.padding),
                    border_radius=ft.border_radius.all(self.size_final),
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                    animate=ft.animation.Animation(duration=self._hover_duration if self._hover_duration else 200, curve=ft.AnimationCurve.DECELERATE),
                ),
                ft.Container(
                    key=self._key,
                    alignment=ft.alignment.center,
                    bgcolor=None,
                    tooltip=self._tooltip,
                    padding=ft.padding.all(self.padding),
                    border_radius=ft.border_radius.all(self.size_final),
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                    animate=ft.animation.Animation(duration=self._hover_duration if self._hover_duration else 200, curve=ft.AnimationCurve.DECELERATE),
                    on_hover=lambda e: self.on_button_hover_event(e),
                    on_click=self._on_click,
                    content=ft.Icon(
                        name=self._icon, 
                        size=self._size, 
                        color=self._color, 
                        opacity=0.5 if self._no_hover else 1,
                        # offset=ft.transform.Offset(x=0, y=-0.1),
                        animate_opacity=ft.animation.Animation(duration=200, curve=ft.AnimationCurve.DECELERATE),
                    )
                ),
            ]
        )

        # self.builder = ft.Container(
        #     key=self._key,
        #     width=self.size_final,
        #     height=self.size_final,
        #     bgcolor=self._bgcolor,
        #     alignment=ft.alignment.center,
        #     tooltip=self._tooltip,
        #     visible=self._visible,
        #     disabled=self._disabled,
        #     border_radius=ft.border_radius.all(self.size_final),
        #     clip_behavior=ft.ClipBehavior.HARD_EDGE,
        #     animate=ft.animation.Animation(duration=220, curve=ft.AnimationCurve.DECELERATE),
        #     on_hover=lambda e: self.on_button_hover_event(e),
        #     on_click=self._on_click,
        #     content=ft.Icon(
        #         name=self._icon, 
        #         size=int(self._size), 
        #         color=self._color, 
        #         opacity=self._opacity,
        #     )
        # )

        return self.builder

class ToastPosition:
    """The toast position attribute.

    Attribute:
        `TOP_CENTER`
        `TOP_LEFT`
        `TOP_RIGHT`
        `BOTTOM_CENTER`
        `BOTTOM_LEFT`
        `BOTTOM_RIGHT`
        `CENTER`
        `CENTER_LEFT`
        `CENTER_RIGHT`
    """
    TOP_CENTER = "top_center"
    TOP_LEFT = "top_left"
    TOP_RIGHT = "top_right"

    BOTTOM_CENTER = "bottom_center"
    BOTTOM_LEFT = "bottom_left"
    BOTTOM_RIGHT = "bottom_right"

    CENTER = "center"
    CENTER_LEFT = "center_left"
    CENTER_RIGHT = "center_right"

class ToastAction(UserControl):
    """ToastAction - Extended from UserControl class."""
    def __init__(self, 
        key: Optional[Any] = None,
        data: Optional[Any] = None,
        text: Optional[str] = None, 
        width: Optional[Union[int, float]]= None, 
        height: Optional[Union[int, float]] = None, 
        url: Optional[str] = None, 
        url_target: Optional[str] = None, 
        on_hover: Callable[[ControlEvent], None] = None, 
        on_click: Callable[[ControlEvent], None] = None, 
        on_long_press: Callable[[ControlEvent], None] = None, 
        disabled: Optional[bool] = None, 
        color: Union[None, str, Dict[Union[str, MaterialState], str]] = None,
        bgcolor: Union[None, str, Dict[Union[str, MaterialState], str]] = None,
        action_style: Optional[Literal["elevated", "filled", "outlined", "texted"]] = None,
        ): # DESC => initialize constructor.
        """Initialize the ToastAction object.

        Args:
            `key` (Any, optional): An optional key to uniquely identify the control. It can be used for custom indexing or identification purposes. Defaults to None.
            `data` (Any, optional): An optional data value associated with the control. This data can be used to store additional information related to the control. Defaults to None.
            `text` (str, optional): The text or label to be displayed on the control. It represents the visible text on the button. Defaults to None.
            `width` (Union[int, float], optional): The width of the control in pixels. If not provided, the width will be automatically determined based on the content. Defaults to None.
            `height` (Union[int, float], optional): The height of the control in pixels. If not provided. Defaults to 28.
            `url` (str, optional): An optional URL to be opened when the control is clicked. If set, on_click event is fired after that. Defaults to None.
            `url_target` (str, optional): An optional target attribute for the URL specified in url. It determines where the URL will be opened, such as "_blank" for a new tab or "_self" for the current tab. Defaults to None.
            `on_hover` (Callable[[ControlEvent], None], optional): A callback function that will be triggered when the mouse pointer hovers over the control. Defaults to None.
            `on_click` (Callable[[ControlEvent], None], optional): A callback function that will be triggered when the control is clicked. Defaults to None.
            `on_long_press` (Callable[[ControlEvent], None], optional): A callback function that will be triggered when the control is long-pressed. Defaults to None.
            `disabled` (bool, optional): A boolean flag that determines whether the control is disabled. If set to True, the control will be non-interactive. Defaults to None.
            `color` (Union[None, str, Dict[Union[str, MaterialState], str]]): The text color of the control. It can be specified as a color string or a dictionary containing mappings for different states {"": "red", "hovered": "blue", ft.MaterialState.FOCUSED: ft.colors.WHITE}. Defaults to None.
            `bgcolor` (Union[None, str, Dict[Union[str, MaterialState], str]]): The background color of the control. It can be specified as a color string or a dictionary containing mappings for different states {"": "red", "hovered": "blue", ft.MaterialState.FOCUSED: ft.colors.WHITE}. Defaults to None.
            `action_style` (str, optional): The style of the button. It can be one of four options: "elevated", "filled", "outlined", or "texted". Defaults to `"texted"`.

        Returns:
            Control:
        """
        super().__init__()
        # DESC => Initialize the state variables attribute.
        self.action_style = action_style

        self.button_texted = ft.TextButton(
            key=key,
            data=data,
            text=text,
            width=width,
            height=height if height else 28,
            url=url,
            url_target=url_target,
            on_hover=on_hover,
            on_long_press=on_long_press,
            on_click=on_click,
            disabled=disabled,
            style=ft.ButtonStyle(
                color=color,
                bgcolor=bgcolor,
                padding={"": ft.padding.only(top=2, bottom=2, left=8, right=8)},
                shape={"": ft.RoundedRectangleBorder(radius=4)},
            )
        )
        self.button_filled = ft.FilledButton(
            key=key,
            data=data,
            text=text,
            width=width,
            height=height if height else 28,
            url=url,
            url_target=url_target,
            on_hover=on_hover,
            on_long_press=on_long_press,
            on_click=on_click,
            disabled=disabled,
            style=ft.ButtonStyle(
                color=color,
                bgcolor=bgcolor,
                padding={"": ft.padding.only(top=2, bottom=2, left=8, right=8)},
                shape={"": ft.RoundedRectangleBorder(radius=4)},
            )
        )
        self.button_elevated = ft.ElevatedButton(
            key=key,
            data=data,
            text=text,
            width=width,
            height=height if height else 28,
            elevation=1,
            url=url,
            url_target=url_target,
            on_hover=on_hover,
            on_long_press=on_long_press,
            on_click=on_click,
            disabled=disabled,
            style=ft.ButtonStyle(
                color=color,
                bgcolor=bgcolor,
                padding={"": ft.padding.only(top=2, bottom=2, left=8, right=8)},
                shape={"": ft.RoundedRectangleBorder(radius=4)},
            )
        )
        self.button_outlined = ft.OutlinedButton(
            key=key,
            data=data,
            text=text,
            width=width,
            height=height if height else 28,
            url=url,
            url_target=url_target,
            on_hover=on_hover,
            on_long_press=on_long_press,
            on_click=on_click,
            disabled=disabled,
            style=ft.ButtonStyle(
                color=color,
                bgcolor=bgcolor,
                padding={"": ft.padding.only(top=2, bottom=2, left=8, right=8)},
                shape={"": ft.RoundedRectangleBorder(radius=4)},
                side={"": ft.BorderSide(width=0.5, color=ft.colors.PRIMARY)}
            )
        )

    def build(self):
        """The initialize build control's UI."""
        if self.action_style == "texted":
            return self.button_texted
        elif self.action_style == "outlined":
            return self.button_outlined
        elif self.action_style == "filled":
            return self.button_filled
        elif self.action_style == "elevated":
            return self.button_elevated
        else:
            # DESC => default texted.
            return self.button_texted

class ToastsFlexible:
    """A class - ToastsFlexible"""
    def __init__(self,
        page: Page,
        icon: ft.icons = None,
        title: Optional[Union[str, Control]] = None,
        desc: Optional[Union[str, Control]] = None,
        bgcolor_title: ft.colors = None,
        bgcolor_desc: ft.colors = None,
        shadow: Optional[Union[BoxShadow, List[BoxShadow]]] = None,
        no_live_time: bool = False,
        position: Optional[ToastPosition] = ToastPosition.TOP_RIGHT,
        actions: Optional[List[ToastAction]] = None,
        actions_alignment: Optional[MainAxisAlignment] = None,
        auto_close: Optional[Union[int, float]] = None,
        width: Optional[Union[int, float]] = None,
        trigger: Optional[Control] = None,

        set_history_title: Optional[str] = None,
        set_history_desc: Optional[str] = None,
        set_history: Optional[Dict] = None,

        interval_update: Optional[Union[int, float]] = None,
        interval_random: Optional[bool] = None,
        refresh_runs: Optional[Union[int, float]] = None,
        ): # DESC => initialize constructor.
        """Initialize the ToastsFlexible object.

        Args:
            `page` (Page): The session start of the page container where the toast will be displayed. a for controls (widgets). It represents the user interface page where the toast will be shown.
            `icon` (ft.icons, optional): The icon to be displayed on the toast. It is an optional argument that allows users to customize the icon shown with the toast message. Defaults to None.
            `title` (Union[str, Control], optional): The title of the toast message. It can be either a string or a Control object. If a Control object is used, the toast's title will be dynamic and update as per the control's value Defaults to None.
            `desc` (Union[str, Control], optional): The description or main content of the toast message. It can be either a string or a Control object, enabling dynamic content display. Defaults to None.
            `bgcolor_title` (ft.colors, optional): The background color of the toast title. This argument allows to customize the background color of the toast title section. Defaults to ft.colors.INVERSE_SURFACE.
            `bgcolor_desc` (ft.colors, optional): The background color of the toast description. This argument allows to customize the background color of the toast description section. Defaults to ft.colors.ON_INVERSE_SURFACE.
            `shadow` (Union[BoxShadow, List[BoxShadow]], optional):  The shadow customization for the toast. can set the shadow properties, to add a shadow effect to the toast. Defaults to None.
            `no_live_time` (bool): That determines whether to show live time text to the toast. If set to True, the toast will not display any time information. Defaults to False.
            `position` (ToastPosition, optional): The position of the toast on the screen. It is an optional argument that allows to set the toast's position to one of the predefined positions, such as top-left etc. Defaults to ToastPosition.TOP_RIGHT.
            `actions` (List[ToastAction], optional):  A list of action buttons to be added to the toast. can provide a list of `ToastAction` objects to create interactive buttons within the toast. Defaults to None.
            `actions_alignment` (MainAxisAlignment, optional): The alignment of the action buttons within the toast. It is an optional argument that allows to set the alignment of the buttons, such as start, end, or center.
            `auto_close` (Union[int, float], optional): The time duration (in seconds) after which the toast will automatically close and disappear. If set to None, the toast will not auto-close. Defaults to None.
            `width` (Union[int, float], optional): The width of the toast in pixels. If not provided. Defaults to 350.
            `trigger` (Control, optional): An optional control that can be used to trigger the display of the toast. If a control with an `on_click` attribute is provided, the toast will be shown when the control is clicked. Defaults to None.
            `set_history_title` (str, optional): An optional title to set for the toast's history entry. This argument is used if use a control in `"title"`, or want to set a specific title for the history entry. Defaults to None.
            `set_history_desc` (str, optional):  An optional description to set for the toast's history entry. This argument is used if use a control in `"desc"`, or want to set a specific description for the history entry. Defaults to None.
            `set_history` (Dict, optional):  A dictionary to store the history of displayed toasts. If provided, the dictionary will be updated with the timestamp, title, description, and time ago when each toast is displayed. Defaults to None.
            `interval_update` (Union[int, float], optional): The time interval (in seconds) between each update of the opening time of the toast. If set, the opening time will be refreshed at the specified interval. Defaults to 5.
            `interval_random` (bool, optional): A boolean flag that determines whether to set a random interval between each update. If set to True, the opening time will be refreshed at random intervals between updates. Defaults to False.
            `refresh_runs` (Union[int, float], optional): The time interval (in seconds) for an refresh loop run. If provided, the opening time will be refreshed continuously at the specified interval until the toast is closed or auto-closes, if use None or set param `auto_close` or set `no_live_time` True you will not update. Defaults to None.

        Example:
        ```python
            toasts_history = {}
            
            # DESC => Toast without trigger.
            button = ft.ElevatedButton("Toast", 
                on_click=lambda _: ToastsFlexible(
                    page=page,
                    icon=ft.icons.INFO,
                    title="Toast without trigger",
                    desc="Toast description",
                    bgcolor_title=None,
                    bgcolor_desc=None,
                    auto_close=None,
                    trigger=None,
                    set_history=toasts_history,
                    position=ToastPosition.TOP_RIGHT,
                    actions=[
                        ToastAction(
                            text="action",
                            action_style="texted",
                            disabled=False,
                            on_click=lambda e: print(e),
                        )
                    ]
                )
            )
            
            # DESC => Toast with trigger and auto close.
            button_trigger = ft.ElevatedButton("Toast")
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

            # DESC => Toast with set interval random.
            button_interval = ft.ElevatedButton("Toast", 
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

            # DESC => Toast title only and interval 1 second update.
            button_title = ft.ElevatedButton("Toast", 
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

            # DESC => Toast description only and auto close.
            button_desc = ft.ElevatedButton("Toast", 
                on_click=lambda _: ToastsFlexible(
                    page=page,
                    desc="Toast description only and auto close.",
                    auto_close=5,
                    position=ToastPosition.TOP_LEFT,
                    set_history_title=".....",
                    set_history=toasts_history,
                )
            )

            # DESC => Toast with description customized and hide live time text.
            button_desc_customized = ft.ElevatedButton("Toast", 
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

            # DESC => Toast with description customized and hide title.
            button_desc_customized_2 = ft.ElevatedButton("Toast", 
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
                            on_click=lambda e: print(e),
                        ),
                        ToastAction(
                            text="Not update",
                            width=100,
                            action_style="outlined",
                            disabled=False,
                            on_click=lambda e: print(e),
                        )
                    ]
                )
            )

            page.add(button, 
                button_trigger, 
                button_interval, 
                button_title, 
                button_desc, 
                button_desc_customized,
                button_desc_customized_2)
            page.update()

            # DESC => output toast history.
            print(toasts_history)
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
        """
        super().__init__()
        # DESC => Initialize the state variables attribute.
        self._page = page
        self._icon = icon
        self._title = title
        self._desc = desc
        self._bgcolor_header = bgcolor_title
        self._bgcolor_content = bgcolor_desc
        self._shadow = shadow
        self._no_live_time = no_live_time
        self._position = position
        self._actions = actions
        self._actions_alignment = actions_alignment
        self._auto_close = auto_close
        self._width = width
        self._trigger = trigger

        self._set_history_title = set_history_title
        self._set_history_desc = set_history_desc
        self._set_history = set_history

        self._interval_update = interval_update
        self._interval_random = interval_random
        self._refresh_runs = refresh_runs

        self.gen_id = GenerateID()
        self.overlay_manger = OverlayPageManger(page=self._page)
        self.stacks_toast_key = self.gen_id.generate_md5_id(f"ToastsFlexible_stacks_{self.position_current(self._position)}")

        # DESC => Release toast to page.
        if self._trigger:
            assert hasattr(self._trigger, "on_click"
            ), "Trigger must contain 'Controls' and 'Control' contain 'on_click' attribute."
            self._trigger.on_click = lambda _: self.open_toast()
        else:
            self.open_toast()

    def position_current(self, pos):
        if pos == ToastPosition.TOP_LEFT:
            return ToastPosition.TOP_LEFT
        elif pos == ToastPosition.TOP_RIGHT:
            return ToastPosition.TOP_RIGHT
        elif pos == ToastPosition.TOP_CENTER:
            return ToastPosition.TOP_CENTER
        elif pos == ToastPosition.BOTTOM_LEFT:
            return ToastPosition.BOTTOM_LEFT
        elif pos == ToastPosition.BOTTOM_RIGHT:
            return ToastPosition.BOTTOM_RIGHT
        elif pos == ToastPosition.BOTTOM_CENTER:
            return ToastPosition.BOTTOM_CENTER
        elif pos == ToastPosition.CENTER:
            return ToastPosition.CENTER
        elif pos == ToastPosition.CENTER_LEFT:
            return ToastPosition.CENTER_LEFT
        elif pos == ToastPosition.CENTER_RIGHT:
            return ToastPosition.CENTER_RIGHT
        else:
            return ToastPosition.TOP_LEFT

    def set_history_toast(self):
        # DESC => Get current time info.
        toast_time = datetime.now()

        if isinstance(self._set_history, Dict):
            # DESC => Add a new name and value to the Dictionary.
            self._set_history.update(
                {   
                    str(self.gen_id.generate_random_id()): {
                        self._title if isinstance(self._title, str) and self._set_history_title is None else self._set_history_title: {
                            "description": self._desc if isinstance(self._desc, str) and self._set_history_desc is None else self._set_history_desc,
                            "ago": {
                                "Year": toast_time.year, 
                                "Month": toast_time.month, 
                                "Day": toast_time.day, 
                                "Hour": toast_time.hour, 
                                "Minute": toast_time.minute, 
                                "Seconds": toast_time.second, 
                            }
                        }
                    }
                }
            )

    def on_close_toast_event(self, event: ControlEvent):
        """Events handler.

        Args:
            `event` (Callable[[ControlEvent], None]): represent any callable object,
                such as a function, a method, or a lambda expression. Defaults to None.

        Returns:
            None
        """
        # DESC => filter and get control in overlay.
        control_stacks_toasts = self.overlay_manger.get_control_specific_with_filtering(
            attribute_control="key",
            attr_value_match=self.stacks_toast_key
        )[0]
        
        for control in control_stacks_toasts.controls[:]:
            # DESC => Check current control.
            if control == self.control_toast:
                # DESC => Remove control in control_stacks_toasts.
                control.opacity = 0
                control_stacks_toasts.controls.remove(control)
                control_stacks_toasts.update()

    def on_auto_disapper_toast(self):
        def update_progress(control: Control, time_second: Union[int, float], start_progress_value: Union[int, float] = 0.0):
            assert hasattr(control, "value"
            ), "control must contain 'value' attribute."

            value = start_progress_value
            while True:
                value += 0.01
                control.value = round(value, 2)
                control.update()

                time_sleep_accuracy(sleep_time=round(0.01 + (time_second - 1) * 0.01, 3), measuring_time="monotonic")
                if control.value == 1.0:
                    return True

        # DESC => filter and get control in overlay.
        control_stacks_toasts = self.overlay_manger.get_control_specific_with_filtering(
            attribute_control="key",
            attr_value_match=self.stacks_toast_key
        )[0]
        
        for control in control_stacks_toasts.controls[:]:
            # DESC => Check current control.
            if control == self.control_toast:
                if update_progress(control=control.content.controls[2], time_second=self._auto_close):
                    # DESC => Remove control in control_stacks_toasts.
                    control.opacity = 0
                    control_stacks_toasts.controls.remove(control)
                    control_stacks_toasts.update()

    def open_toast(self):
        """Append control's UI in overlay to page."""
        def update_control_value(control, interval_update, interval_random = True, refresh_runs = None):
            """Update control value.

            Args:
                `interval_update` (Union[int, float]): The time interval (in seconds) between each update.
                `interval_random` (Union[int, float]): When true sets the random interval between each update.
                `refresh_runs` (int): The time interval (in seconds) of the an refresh loop run.
            """
            start_time = time.time()
            elapsed_time = 0

            if refresh_runs is not None:
                if interval_update is None:
                    _interval_update = 5
                else:
                    _interval_update = interval_update

                while elapsed_time < (refresh_runs +1):
                    # DESC => filter and get control in overlay.
                    control_stacks_toasts = self.overlay_manger.get_control_specific_with_filtering(
                        attribute_control="key",
                        attr_value_match=self.stacks_toast_key
                    )[0]

                    if interval_random:
                        _interval_update = random.uniform(0.5, 10)

                    # DESC => Check exists control.
                    if control in control_stacks_toasts.controls:
                        # DESC => The modulo operator % to check if the current_time is divisible evenly by 1 
                        # (i.e., it's an integer multiple of 1 second).
                        if elapsed_time % _interval_update != 0:
                            if elapsed_time >= 60:
                                control.content.controls[0].content.controls[1].controls[0].value = f"{int(elapsed_time)} minute ago"
                            else:
                                control.content.controls[0].content.controls[1].controls[0].value = f"{int(elapsed_time)} seconds ago"
                            control.update()
                    else:
                        break

                    elapsed_time = round(time.time() - start_time, 2)
                    time.sleep(_interval_update)

        def set_stacks_toasts(toast_positions: str):
            if toast_positions == ToastPosition.TOP_LEFT: 
                position = SetPosition.top_left
                vertical_alignment = ft.MainAxisAlignment.START
                horizontal_alignment = ft.CrossAxisAlignment.START
            elif toast_positions == ToastPosition.TOP_RIGHT:
                position = SetPosition.top_right
                vertical_alignment = ft.MainAxisAlignment.START
                horizontal_alignment = ft.CrossAxisAlignment.END
            elif toast_positions == ToastPosition.TOP_CENTER:
                position = SetPosition.top_center
                vertical_alignment = ft.MainAxisAlignment.START
                horizontal_alignment = ft.CrossAxisAlignment.CENTER
            elif toast_positions == ToastPosition.BOTTOM_LEFT:
                position = SetPosition.bottom_left
                vertical_alignment = ft.MainAxisAlignment.END
                horizontal_alignment = ft.CrossAxisAlignment.START
            elif toast_positions == ToastPosition.BOTTOM_RIGHT:
                position = SetPosition.bottom_right
                vertical_alignment = ft.MainAxisAlignment.END
                horizontal_alignment = ft.CrossAxisAlignment.END
            elif toast_positions == ToastPosition.BOTTOM_CENTER:
                position = SetPosition.bottom_center
                vertical_alignment = ft.MainAxisAlignment.END
                horizontal_alignment = ft.CrossAxisAlignment.CENTER
            elif toast_positions == ToastPosition.CENTER:
                position = SetPosition.center
                vertical_alignment = ft.MainAxisAlignment.START
                horizontal_alignment = ft.CrossAxisAlignment.CENTER
            elif toast_positions == ToastPosition.CENTER_LEFT:
                position = SetPosition.center_left
                vertical_alignment = ft.MainAxisAlignment.START
                horizontal_alignment = ft.CrossAxisAlignment.START
            elif toast_positions == ToastPosition.CENTER_RIGHT:
                position = SetPosition.center_right
                vertical_alignment = ft.MainAxisAlignment.START
                horizontal_alignment = ft.CrossAxisAlignment.END
            else:
                # DESC => default top_left.
                position = SetPosition.top_left
                vertical_alignment = ft.MainAxisAlignment.START
                horizontal_alignment = ft.CrossAxisAlignment.START

            stacks_toast_control = ft.Column(
                key=self.stacks_toast_key,
                top=position[0]+40 if isinstance(position[0], (int, float)) else position[0],
                left=position[1]+40 if isinstance(position[1], (int, float)) else position[1],
                right=position[2]+40 if isinstance(position[2], (int, float)) else position[2],
                bottom=position[3]+40 if isinstance(position[3], (int, float)) else position[3],
                alignment=vertical_alignment,
                horizontal_alignment=horizontal_alignment,
                spacing=5,
                expand=None
            )

            return stacks_toast_control

        stacks_toasts = set_stacks_toasts(toast_positions=self._position)
        
        # DESC => Append control in overlay or get a control.
        control_stacks_toasts = self.overlay_manger.append_controls_with_filtering(
            controls=stacks_toasts,
            attribute_control="key",
            attr_value_match=self.stacks_toast_key
        )[0]

        control_toast_ui = self.build_toast()

        control_stacks_toasts.controls.append(control_toast_ui)
        control_stacks_toasts.update()
        
        if self._set_history is not None:
            self.set_history_toast()

        if self._auto_close:
            if self._title:
                if self._no_live_time is False:
                    # DESC => Update control text of toast header right show time.
                    control_toast_ui.content.controls[0].content.controls[1].controls[0].value = "just now"
                    control_toast_ui.content.controls[0].content.controls[1].controls[0].update()
            self.on_auto_disapper_toast()
        else:
            if self._title:
                if self._no_live_time is False:
                    # DESC => Update control text of toast header right show time.
                    control_toast_ui.content.controls[0].content.controls[1].controls[0].value = "just now"
                    control_toast_ui.content.controls[0].content.controls[1].controls[0].update()
                    update_control_value(control=control_toast_ui, interval_update=self._interval_update, interval_random=self._interval_random, refresh_runs=self._refresh_runs)

    def build_toast(self):
        """The initialize build control's UI."""
        self._color_progress = set_color_balance(bgcolor=self._bgcolor_header) if (
            self._bgcolor_header and self._title) else set_color_balance(bgcolor=self._bgcolor_content) if (
            self._bgcolor_content and self._desc) else ft.colors.INVERSE_PRIMARY

        self._bgcolor_progress = ft.colors.SURFACE_VARIANT if (
            self._color_progress == ft.colors.INVERSE_PRIMARY) else self._bgcolor_header if (
            self._bgcolor_header and self._title) else self._bgcolor_content if (
            self._bgcolor_content and self._desc) else ft.colors.SURFACE_VARIANT # DESC => Set default ft.colors.SURFACE_VARIANT

        self._icon = self._icon if self._icon else None # DESC => Set default ft.icons.INFO.
        self._width = self._width if self._width else 350 # DESC => Set default 350.
        self._bgcolor_header = self._bgcolor_header if self._bgcolor_header else ft.colors.INVERSE_SURFACE # DESC => Set default ft.colors.INVERSE_SURFACE
        self._bgcolor_content = self._bgcolor_content if self._bgcolor_content else ft.colors.ON_INVERSE_SURFACE # DESC => Set default ft.colors.ON_INVERSE_SURFACE

        # DESC => Control of toast container.
        self.control_toast = ft.Container(
            width=self._width,
            # border=ft.border.all(width=0.4, color=ft.colors.with_opacity(opacity=0.25, color=ft.colors.INVERSE_SURFACE)),
            border_radius=ft.border_radius.all(value=7),
            shadow=self._shadow if self._shadow else ft.BoxShadow(spread_radius=0.01, blur_radius=0.3, color=ft.colors.with_opacity(0.25, ft.colors.SHADOW), offset=ft.transform.Offset(x=0, y=1)),
            opacity=1,
            animate_opacity=ft.Animation(duration=500, curve=ft.AnimationCurve.DECELERATE),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                spacing=0,
                controls=[
                    # DESC => Control of toast header.
                    ft.Container(
                        bgcolor=ft.colors.with_opacity(opacity=0.9, color=self._bgcolor_header),
                        padding=ft.padding.only(left=9, top=7, right=8, bottom=7),
                        height=20+14+5,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=15,
                            controls=[
                                # DESC => Control of toast header left.
                                ft.Row(
                                    expand=True,
                                    alignment=ft.MainAxisAlignment.START,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=8 if self._icon and self._title else 0,
                                    controls=[
                                        ft.Icon(
                                            name=self._icon,
                                            size=20,
                                            color=set_color_balance(bgcolor=self._bgcolor_header),
                                        ) if self._icon else ft.VerticalDivider(width=0, color=ft.colors.TRANSPARENT), 

                                        ft.Text(
                                            expand=True,
                                            value=self._title,
                                            weight=ft.FontWeight.W_400,
                                            color=set_color_balance(bgcolor=self._bgcolor_header),
                                            style=ft.TextThemeStyle.BODY_MEDIUM,
                                            overflow=ft.TextOverflow.ELLIPSIS
                                        ) if self._title else ft.VerticalDivider(width=0, color=ft.colors.TRANSPARENT), 
                                    ]
                                ),
                                
                                # DESC => Control of toast header right.
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.END,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=8 if (self._auto_close is None and self._actions and self._desc is None) else 5 if (self._actions and self._desc is None) else 3 if (self._auto_close is None and self._actions is None and self._desc is None) else 3,
                                    controls=[
                                        # DESC => Control of toast header show time.
                                        ft.Text(
                                            value=None,
                                            weight=ft.FontWeight.W_100,
                                            style=ft.TextThemeStyle.BODY_SMALL,
                                            opacity=0.7,
                                            color=set_color_balance(bgcolor=self._bgcolor_header),
                                        ) if self._no_live_time is False else ft.VerticalDivider(width=1, color=ft.colors.TRANSPARENT),

                                        # DESC => Control of toast header actions.
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.END,
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=5,
                                            controls=self._actions
                                        ) if self._actions and self._desc is None else ft.VerticalDivider(width=0, color=ft.colors.TRANSPARENT),
                                        
                                        # DESC => Control of toast header button close.
                                        ButtonIcon(
                                            icon=ft.icons.CLOSE_OUTLINED,
                                            size=20,
                                            no_hover=True,
                                            on_click=lambda e: self.on_close_toast_event(e),
                                            color=set_color_balance(bgcolor=self._bgcolor_header),
                                        ) if self._auto_close is None else ft.VerticalDivider(width=0, color=ft.colors.TRANSPARENT),
                                    ]
                                ),
                            ]
                        )
                    ) if self._title else ft.Divider(height=0, color=ft.colors.TRANSPARENT),

                    # DESC => Control of toast content.
                    ft.Container(
                        width=self._width,
                        bgcolor=ft.colors.with_opacity(opacity=0.9, color=self._bgcolor_content),
                        padding=ft.padding.only(left=9, top=10, right=8, bottom=10),
                        content=ft.Column(
                            spacing=10 if self._actions else 0,
                            controls=[
                                # DESC => Control of toast content messages.
                                ft.Row(
                                    width=self._width,
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    vertical_alignment=ft.CrossAxisAlignment.START,
                                    controls=[
                                        # DESC => Control of toast text messages.
                                        ft.Text(
                                            expand=True,
                                            value=self._desc,
                                            weight=ft.FontWeight.W_200,
                                            style=ft.TextThemeStyle.BODY_MEDIUM,
                                            color=set_color_balance(bgcolor=self._bgcolor_content)
                                        ) if isinstance(self._desc, str) else self._desc,
                                        
                                        # DESC => Control of toast content button close.
                                        ButtonIcon(
                                            icon=ft.icons.CLOSE_OUTLINED,
                                            size=20,
                                            no_hover=True,
                                            on_click=lambda e: self.on_close_toast_event(e),
                                            color=set_color_balance(bgcolor=self._bgcolor_content),
                                        ) if (self._title or self._auto_close) is None else ft.VerticalDivider(width=0, color=ft.colors.TRANSPARENT),
                                    ]
                                ),
                                
                                # DESC => Control of toast content actions.
                                ft.Row(
                                    alignment=self._actions_alignment if self._actions_alignment else ft.MainAxisAlignment.END,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=10,
                                    controls=self._actions
                                ) if self._actions else ft.Divider(height=0, color=ft.colors.TRANSPARENT),
                            ]
                        ),
                    ) if self._desc else ft.Divider(height=0, color=ft.colors.TRANSPARENT),

                    # DESC => Control of toast animation timer.
                    ft.ProgressBar(
                        width=self._width,
                        color=self._color_progress,
                        bgcolor=ft.colors.with_opacity(opacity=0.9, color=self._bgcolor_progress),
                        bar_height=1.5,
                        value=0,
                    ) if self._auto_close else ft.Divider(height=0, color=ft.colors.TRANSPARENT),
                ]
            )
        )
        return self.control_toast
