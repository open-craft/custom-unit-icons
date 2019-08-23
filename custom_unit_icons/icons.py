def get_icon(unit):
    """
    Get icon specified in modulestore.
    If `default` is specified there, make a fallback to the default implementation.
    """
    icon = getattr(unit, 'icon', 'default')
    if icon == 'default':
        return getattr(unit, 'get_icon_class', lambda: 'other')()
    return icon
