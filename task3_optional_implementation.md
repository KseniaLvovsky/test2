# Task 3 — Optional Small Implementation

Complete `answers/task3_optional_solution.py`.

## Goal

Write a small function that validates whether a request body for `POST /v1/audio/jobs` is minimally valid.

## Requirements

Implement a function named `validate_payload(payload)` that returns a list of validation errors.

Rules:
- `user_id` is required and must be a positive integer.
- `text` is required and must be a non-empty string after trimming spaces.
- `voice` is optional, but if present must be one of: `alloy`, `nova`, `echo`.
- `speed` is optional, but if present must be a number between `0.5` and `2.0` inclusive.
- `format` is optional, but if present must be `mp3` or `wav`.

Examples:
- Valid payload => return `[]`
- Invalid payload => return a list such as `['user_id must be a positive integer', 'text is required']`

Do not use external libraries.
