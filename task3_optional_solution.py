def validate_payload(payload):
    errors = []

    # TODO: implement validation rules here

    return errors


if __name__ == "__main__":
    sample_payload = {
        "user_id": 123,
        "text": "Hello world",
        "voice": "alloy",
        "speed": 1.0,
        "format": "mp3",
    }
    print(validate_payload(sample_payload))
