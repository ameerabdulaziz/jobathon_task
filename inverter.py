def invert(s):
    """Accepts a string and returns a string"""
    if isinstance(s, str) or s is None:
        if s is None or len(s) == 0:
            return ''
        elif len(s) == 1:
            return s
        else:
            return s[::-1]
    else:
        return 'Your input is not a string type!'