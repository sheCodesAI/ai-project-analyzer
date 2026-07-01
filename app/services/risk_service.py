def calculate_risk(missing_information: list[str]) -> str:
    """
    Calculate project risk based on missing critical information.
    """

    critical_fields = {
        "final glass thickness",
        "glass thickness",
        "load requirements",
        "structural drawings",
        "project dimensions",
        "location",
    }

    missing_critical = sum(
        1 for item in missing_information
        if item.lower() in critical_fields
    )

    if missing_critical >= 3:
        return "High"

    if missing_critical >= 1:
        return "Medium"

    return "Low"
