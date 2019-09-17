def get_icon(prev_fn, unit):
    """
    Get icon specified in modulestore.
    If `default` is specified there, make a fallback to the default implementation.
    """
    icon = getattr(unit, 'icon', 'default')
    if icon == 'default':
        return prev_fn(unit)
    return icon
