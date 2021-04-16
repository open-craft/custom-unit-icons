from xblock.fields import String, Scope

# Make '_' a no-op so we can scrape strings
# Using lambda instead of `django.utils.translation.ugettext_noop` because Django cannot be imported in this file
_ = lambda text: text


class IconOverrideMixin:
    """ Allow changing the icon used for this specific instance of this XBlock """

    def __init__(self):
        pass

    icon_override = String(
        display_name=_("Icon Override"),
        default='default',
        help=_("XBlock Icon Override"),
        scope=Scope.settings,
    )

def get_icon(prev_fn, unit):
    """
    Get icon specified in modulestore.
    If `default` is specified there, make a fallback to the default implementation.
    """
    icon = getattr(unit, 'icon_override', 'default')
    if icon == 'default':
        return prev_fn(unit)
    return icon

def create_xblock_info(prev_fn, xblock, *args, **kwargs):
    """
    Get icon specified in modulestore.
    If `default` is specified there, make a fallback to the default implementation.
    """
    xblock_info = prev_fn(xblock, *args, **kwargs)
    xblock_info['icon'] = xblock.icon_override
    return xblock_info
