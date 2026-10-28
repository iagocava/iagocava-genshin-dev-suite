PRIMOGEMS_PER_PULL = 160


def calculate_total_pulls(
    primogems: int,
    intertwined_fates: int,
) -> int:
    """Calculate the total number of available pulls."""

    if primogems < 0:
        raise ValueError("Primogems cannot be negative.")

    if intertwined_fates < 0:
        raise ValueError("Intertwined Fates cannot be negative.")

    pulls_from_primogems = primogems // PRIMOGEMS_PER_PULL

    return pulls_from_primogems + intertwined_fates