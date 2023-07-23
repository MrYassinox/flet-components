########################################################################################################################
# TODO DOCUMENT
########################################################################################################################
# |   ├──  |
# |   |    └── src: 
########################################################################################################################
# TODO IMPORTING NECESSARY LIBRARYIES
########################################################################################################################
# LIB python libraryies
from typing import List, Any, Dict, Set, Callable, Union, Tuple, Iterable, Literal, Optional

# LIB => flet libraryies
import flet as ft
from flet import Control, Page

########################################################################################################################
# TODO SET UP
########################################################################################################################
def set_color_balance(bgcolor: str):
    """set color balance.

    Args:
        `bgcolor` (str): The color to background of control.

    Returns:
        str: Returns the color correct to control.
    """
    if bgcolor == ft.colors.PRIMARY:
        color = ft.colors.SURFACE
    elif bgcolor == ft.colors.SECONDARY:
        color = ft.colors.SURFACE
    elif bgcolor == ft.colors.ERROR:
        color = ft.colors.SURFACE
    elif bgcolor == ft.colors.TERTIARY:
        color = ft.colors.SURFACE
    elif bgcolor == ft.colors.OUTLINE:
        color = ft.colors.SURFACE
    elif bgcolor == ft.colors.ON_SURFACE:
        color = ft.colors.SURFACE
    elif bgcolor == ft.colors.ON_BACKGROUND:
        color = ft.colors.SURFACE

    elif bgcolor == ft.colors.SURFACE:
        color = ft.colors.ON_SURFACE
    elif bgcolor == ft.colors.BACKGROUND:
        color = ft.colors.ON_SURFACE
    elif bgcolor == ft.colors.SURFACE_VARIANT:
        color = ft.colors.ON_SURFACE
    elif bgcolor == ft.colors.OUTLINE_VARIANT:
        color = ft.colors.ON_SURFACE
    elif bgcolor == ft.colors.INVERSE_PRIMARY:
        color = ft.colors.ON_SURFACE
    elif bgcolor == ft.colors.ON_INVERSE_SURFACE:
        color = ft.colors.ON_SURFACE

    elif bgcolor == ft.colors.ON_SURFACE_VARIANT:
        color = ft.colors.SURFACE_VARIANT
    elif bgcolor == ft.colors.SURFACE_TINT:
        color = ft.colors.SURFACE_VARIANT

    elif bgcolor == ft.colors.INVERSE_SURFACE:
        color = ft.colors.ON_INVERSE_SURFACE

    elif bgcolor == ft.colors.ON_PRIMARY:
        color = ft.colors.PRIMARY
    elif bgcolor == ft.colors.PRIMARY_CONTAINER:
        color = ft.colors.ON_PRIMARY_CONTAINER
    elif bgcolor == ft.colors.ON_PRIMARY_CONTAINER:
        color = ft.colors.PRIMARY_CONTAINER

    elif bgcolor == ft.colors.ON_SECONDARY:
        color = ft.colors.SECONDARY
    elif bgcolor == ft.colors.SECONDARY_CONTAINER:
        color = ft.colors.ON_SECONDARY_CONTAINER
    elif bgcolor == ft.colors.ON_SECONDARY_CONTAINER:
        color = ft.colors.SECONDARY_CONTAINER

    elif bgcolor == ft.colors.ON_TERTIARY:
        color = ft.colors.TERTIARY
    elif bgcolor == ft.colors.TERTIARY_CONTAINER:
        color = ft.colors.ON_TERTIARY_CONTAINER
    elif bgcolor == ft.colors.ON_TERTIARY_CONTAINER:
        color = ft.colors.TERTIARY_CONTAINER

    elif bgcolor == ft.colors.ON_ERROR:
        color = ft.colors.ERROR
    elif bgcolor == ft.colors.ERROR_CONTAINER:
        color = ft.colors.ON_ERROR_CONTAINER
    elif bgcolor == ft.colors.ON_ERROR_CONTAINER:
        color = ft.colors.ERROR_CONTAINER
    else:
        color = ft.colors.SURFACE
    return color

class SetPosition:
    """The set position attribute.

    Attribute:
        `top_center`: The returns list of top, left, right, bottom.
        `top_left`: The returns list of top, left, right, bottom.
        `top_right`: The returns list of top, left, right, bottom.
        `bottom_center`: The returns list of top, left, right, bottom.
        `bottom_left`: The returns list of top, left, right, bottom.
        `bottom_right`: The returns list of top, left, right, bottom.
        `center`: The returns list of top, left, right, bottom.
        `center_left`: The returns list of top, left, right, bottom.
        `center_right`: The returns list of top, left, right, bottom.
    """
    def _set_position(
        top: Optional[Union[int, float]], 
        left: Optional[Union[int, float]], 
        right: Optional[Union[int, float]], 
        bottom: Optional[Union[int, float]]
        ):
        """Set position.

        Args:
            `top` (Optional[Union[int, float]]): _description_
            `left` (Optional[Union[int, float]]): _description_
            `right` (Optional[Union[int, float]]): _description_
            `bottom` (Optional[Union[int, float]]): _description_

        Returns:
            list: top, left, right, bottom
        """
        return top, left, right, bottom

    top_center      = _set_position(top=0, left=0, right=0, bottom=None)
    """Returns: top, left, right, bottom."""

    top_left        = _set_position(top=0, left=0, right=None, bottom=None)
    """Returns: top, left, right, bottom."""

    top_right       = _set_position(top=0, left=None, right=0, bottom=None)
    """Returns: top, left, right, bottom."""

    bottom_center   = _set_position(top=None, left=0, right=0, bottom=0)
    """Returns: top, left, right, bottom."""

    bottom_left     = _set_position(top=None, left=0, right=None, bottom=0)
    """Returns: top, left, right, bottom."""

    bottom_right    = _set_position(top=None, left=None, right=0, bottom=0)
    """Returns: top, left, right, bottom."""

    center          = _set_position(top=0, left=0, right=0, bottom=0)
    """Returns: top, left, right, bottom."""

    center_left     = _set_position(top=0, left=0, right=None, bottom=0)
    """Returns: top, left, right, bottom."""

    center_right    = _set_position(top=0, left=None, right=0, bottom=0)
    """Returns: top, left, right, bottom."""

class OverlayPageManger:
    """A class OverlayPageManger the an manages the control controls of in page overlay.

    Methods:
        `get_controls`: Get all controls in overlay list.
        `get_control_specific`: Get control specific in overlay list.
        `get_control_specific_with_filtering`: Get control specific with filtering of in overlay list.
        `remove_control_specific_with_filtering`: Remove control specific with filtering of in overlay list.
        `remove_control_specific_with_same`: Remove control specific with if same of in overlay list.
        `append_controls`: Append controls with check if same of in overlay list.
        `append_controls_with_filtering`: Append controls with filtering and check of in overlay list.
        `append_controls_in_specific_route`: Append control in specific page route to display.
        `append_controls_in_specific_route_with_filtering`: Append control in specific page route to display with filtering and check of in overlay.
        `clear_overlay`: Clear controls into overlay list.
    """
    def __init__(self, page: Page): # DESC => initialize constructor.
        """Initialize the OverlayPageManger object.

        Args:
            `page` (Page): The session start of page container to displaying a for controls (widgets).
        """
        super().__init__()
        # DESC => Initialize the state variables attribute.
        self.page = page

    def get_controls(self, page: Optional[Page] = None):
        """Get all controls in overlay list.

        Args:
            `page` (Page, optional): The session start of page container to displaying a for controls (widgets). Defaults to None.

        Returns:
            List: return the all controls in overlay list.
        """
        return page.overlay if page else self.page.overlay

    def get_control_specific(self, control: Control, page: Optional[Page] = None):
        """Get control specific in overlay list.

        Args:
            `page` (Page, optional): The session start of page container to displaying a for controls (widgets). Defaults to None. 
            `control` (Control): The Control object specific of the getting it.

        Returns:
            Control: return control object.
        """
        if page:
            if control in page.overlay:
                return page.overlay[page.overlay.index(control)]
            else:
                return None
        else:
            if control in self.page.overlay:
                return self.page.overlay[self.page.overlay.index(control)]
            else:
                return None

    def get_control_specific_with_filtering(self, attribute_control: str, attr_value_match: str, page: Optional[Page] = None):
        """Get control specific with filtering of in overlay list.

        Args:
            `page` (Page, optional): The session start of page container to displaying a for controls (widgets). Defaults to None. 
            `attribute_control` (str): The attribute of control example "key" or "data" etc.
            `attr_value_match` (str): The value of match to searching in attribute value.

        Returns:
            List: Returns each control containing attribute value of match in list.
        """
        # DESC => filter and get control in overlay list.
        return list(filter(lambda control: getattr(control, attribute_control) == attr_value_match, page.overlay if page else self.page.overlay))

    def remove_control_specific_with_filtering(self, attribute_control: str, attr_value_match: str, page: Optional[Page] = None):
        """Remove control specific with filtering of in overlay list.

        Args:
            `page` (Page, optional): The session start of page container to displaying a for controls (widgets). Defaults to None. 
            `attribute_control` (str): The attribute of control example "key" or "data" etc.
            `attr_value_match` (str): The value of match to searching in attribute value.

        Returns:
            None.
        """
        _page = page if page else self.page

        # DESC => filter and get control in overlay list.
        controls_filter = list(filter(lambda control: getattr(control, attribute_control) == attr_value_match, _page.overlay))

        for control in controls_filter[:]:
            if control in _page.overlay:
                _page.overlay.remove(control)
                controls_filter.remove(control)
        _page.update()

    def remove_control_specific_with_same(self, control_compring: Control, page: Optional[Page] = None):
        """Remove control specific with if same of in overlay list.

        Args:
            `page` (Page, optional): The session start of page container to displaying a for controls (widgets). Defaults to None. 
            `control_compring` (Control): The Control object specific of the comparing if same it.

        Returns:
            None.
        """
        _page = page if page else self.page

        for control in _page.overlay[:]:
            if control == control_compring:
                _page.overlay.remove(control)
        _page.update()
    
    def append_controls(self, controls: Control, page: Optional[Page] = None):
        """Append controls with check if same of in overlay list.

        Args:
            `page` (Page, optional): The session start of page container to displaying a for controls (widgets). Defaults to None. 
            `controls` (Control): The Control object to append in overlay to page.

        Returns:
            (Control): returns Control object f append or available into overlay.
        """
        _page = page if page else self.page

        # DESC => Check controls if not in overlay to page.
        if controls not in _page.overlay:
            # DESC => Append control's UI in overlay to page to display.
            _page.overlay.append(controls)
            _page.update()
            return controls
        else:
            return controls

    def append_controls_with_filtering(self, controls: Control, attribute_control: str, attr_value_match: str, page: Optional[Page] = None):
        """Append controls with filtering and check of in overlay list.

        Args:
            `page` (Page, optional): The session start of page container to displaying a for controls (widgets). Defaults to None.
            `controls` (Control): The Control object to append in overlay to page.
            `attribute_control` (str): The attribute of control example "key" or "data" etc.
            `attr_value_match` (str): The value of match to searching in attribute value.

        Returns:
            (list[Control]): returns list Controls objects if append or available into overlay.
        """
        _page = page if page else self.page

        # DESC => filter and get control in overlay list.
        filtering = self.get_control_specific_with_filtering(attribute_control=attribute_control, attr_value_match=attr_value_match, page=_page)
        
        # DESC => Check controls if not in overlay to page.
        if len(filtering) == 0:
            # DESC => Append control's UI in overlay to page to display.
            _page.overlay.append(controls)
            _page.update()
            return [controls]
        else:
            return filtering

    def append_controls_in_specific_route(self, controls: Control, route_display: str, page: Optional[Page] = None):
        """Append control in specific page route to display.

        Args:
            `page` (Page, optional): The session start of page container to displaying a for controls (widgets). Defaults to None. 
            `controls` (Control): The Control object to append in overlay to page.
            `route_display` (str): The specific page route to display controls.

        Returns:
            (Control): returns Control object if append or available on overlay list.
        """
        _page = page if page else self.page

        # DESC => Check current page navigation route.
        if _page.route == route_display:
            if controls not in _page.overlay:
                # DESC => Append control's UI in overlay to page to display.
                _page.overlay.append(controls)
                _page.update()
                return controls
            else:
                return controls
        else:
            self.remove_control_specific_with_same(control_compring=controls, page=_page)

    def append_controls_in_specific_route_with_filtering(self, controls: Control, attribute_control: str, attr_value_match: str, route_display: str, page: Optional[Page] = None):
        """Append control in specific page route to display with filtering and check of in overlay.

        Args:
            `page` (Page, optional): The session start of page container to displaying a for controls (widgets). Defaults to None. 
            `controls` (Control): The Control object to append in overlay to page.
            `attribute_control` (str): The attribute of control example "key" or "data" etc.
            `attr_value_match` (str): The value of match to searching in attribute value.
            `route_display` (str): The specific page route to display controls.

        Returns:
            (list[Control]): returns list Controls objects if append or available into overlay.
        """
        _page = page if page else self.page

        # DESC => filter and get control in overlay list.
        filtering = self.get_control_specific_with_filtering(
            attribute_control=attribute_control, attr_value_match=attr_value_match, page=_page)

        # DESC => Check current page navigation route.
        if _page.route == route_display:
            # DESC => Check controls if not in overlay to page.
            if len(filtering) == 0:
                # DESC => Append control's UI in overlay to page to display.
                _page.overlay.append(controls)
                _page.update()
                return [controls]
            else:
                return filtering
        else:
            # DESC => Check controls if not in overlay to page.
            for control in filtering[:]:
                if control in _page.overlay:
                    _page.overlay.remove(control)
                    filtering.remove(control)

    def clear_overlay(self, page: Optional[Page] = None):
        """Clear controls into overlay list.

        Args:
            `page` (Page, optional): The session start of page container to displaying a for controls (widgets). Defaults to None. 

        Returns:
            None.
        """
        _page = page if page else self.page

        # DESC => Clear controls in overlay list.
        _page.overlay.clear()
        _page.update()
