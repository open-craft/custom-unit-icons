from xblock.fields import Integer, String, Scope

# Make '_' a no-op so we can scrape strings
# Using lambda instead of `django.utils.translation.ugettext_noop` because Django cannot be imported in this file
_ = lambda text: text


class IconOverrideMixin:
    """Allow changing the icon used for this specific instance of this XBlock"""

    def __init__(self):
        pass

    icon_override = String(
        display_name=_("Icon Override"),
        default='default',
        help=_("XBlock Icon Override"),
        scope=Scope.settings,
    )

    # DEPRECATED: We have been using the `icon` field in the modulestore before introducing the `icon_override` one.
    #  The `icon` field and the `ICON_MAPPING` list are used by the existing courses, which have been created the
    #  "old" way. These were introduced for keeping the backward compatibility and should be treated as read-only.
    icon = Integer(
        display_name=_("Deprecated Icon Override"),
        default=0,
        help=_("Deprecated XBlock Icon Override ID"),
        scope=Scope.settings,
    )

    ICON_MAPPING = [
        icon_override.default,
        'text',
        'video',
        'interactive',
        'downloadable',
        'ask-question',
        'assess-question',
        'text-box',
    ]


def get_icon(prev_fn, unit):
    """
    Get icon specified in the modulestore.

    If a default value is specified there, make a fallback to a default implementation.
    """
    icon = getattr(unit, 'icon_override', IconOverrideMixin.icon_override.default)

    # DEPRECATED: This check is here for supporting the deprecated `icon` field.
    if icon == IconOverrideMixin.icon_override.default:
        icon_id = getattr(unit, 'icon', 0)
        if icon_id >= len(IconOverrideMixin.ICON_MAPPING):
            icon_id = 0
        icon = IconOverrideMixin.ICON_MAPPING[icon_id]

    if icon == IconOverrideMixin.icon_override.default:
        return prev_fn(unit)
    return icon


def create_xblock_info(prev_fn, xblock, *args, **kwargs):
    """
    Create the information needed for client-side XBlockInfo with the original implementation and add an icon
    field there, so it can be retrieved in the Studio.
    """
    xblock_info = prev_fn(xblock, *args, **kwargs)
    xblock_info['icon'] = get_icon(lambda _: IconOverrideMixin.icon_override.default, xblock)
    return xblock_info
