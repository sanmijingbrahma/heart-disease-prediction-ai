def get_risk_label(prediction: int) -> str:
    if prediction == 0:
        return "Low Risk"
    elif prediction == 1:
        return "High Risk"
    return "Unknown"


def format_probability(probability: float) -> str:
    return f"{probability * 100:.2f}%"


def validate_input(patient: dict) -> tuple[bool, str]:
    if not patient:
        return False, "Patient data is empty."

    for field, value in patient.items():
        if value is None:
            return False, f"Missing value for '{field}'."

    return True, "Validation successful."
