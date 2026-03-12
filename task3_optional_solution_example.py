def validate_payload(payload):
    errors = []

    if not isinstance(payload, dict):
        return ["payload must be a dictionary"]

    user_id = payload.get("user_id")
    if not isinstance(user_id, int) or user_id <= 0:
        errors.append("user_id must be a positive integer")

    text = payload.get("text")
    if not isinstance(text, str) or text.strip() == "":
        errors.append("text is required")

    if "voice" in payload:
        allowed_voices = {"alloy", "nova", "echo"}
        if payload["voice"] not in allowed_voices:
            errors.append("voice must be one of: alloy, nova, echo")

    if "speed" in payload:
        speed = payload["speed"]
        if not isinstance(speed, (int, float)) or speed < 0.5 or speed > 2.0:
            errors.append("speed must be between 0.5 and 2.0")

    if "format" in payload:
        if payload["format"] not in {"mp3", "wav"}:
            errors.append("format must be mp3 or wav")

    return errors


if __name__ == "__main__":
    examples = [
        {"user_id": 1, "text": "hello"},
        {"user_id": 0, "text": "hello", "voice": "robot"},
        {"user_id": 2, "text": "   ", "speed": 3, "format": "aac"},
    ]

    for item in examples:
        print(item)
        print(validate_payload(item))
        print("---")
