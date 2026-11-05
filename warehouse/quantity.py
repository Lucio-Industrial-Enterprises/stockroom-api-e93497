"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return a non-negative integer quantity parsed from *value*.

    Raises ValueError for blank input, non-integer strings, or negative values.
    """
    qty = int(value.strip())
    if qty < 0:
        raise ValueError("quantity must not be negative")
    return qty
