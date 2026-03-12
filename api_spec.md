# API Spec — Audio Job Creation

## Endpoint
`POST /v1/audio/jobs`

## Description
Creates an asynchronous audio generation job from text input.

## Request body

```json
{
  "user_id": 123,
  "text": "Hello world",
  "voice": "alloy",
  "speed": 1.0,
  "format": "mp3"
}
```

## Field definitions

- `user_id` — required integer
- `text` — required string, maximum 5000 characters
- `voice` — optional string, supported values: `alloy`, `nova`, `echo`
- `speed` — optional number, expected range 0.5 to 2.0
- `format` — optional string, supported values: `mp3`, `wav`

## Expected successful response

**201 Created**

```json
{
  "job_id": "job_98765",
  "status": "queued",
  "created_at": "2026-03-11T14:25:00Z"
}
```

## Possible error responses

- `400 Bad Request` — malformed JSON
- `401 Unauthorized` — missing or invalid auth
- `403 Forbidden` — authenticated but not allowed
- `404 Not Found` — endpoint not found
- `409 Conflict` — duplicate request or conflicting state
- `413 Payload Too Large` — text too large
- `415 Unsupported Media Type` — invalid content type
- `422 Unprocessable Entity` — validation errors
- `429 Too Many Requests` — rate limit exceeded
- `500 Internal Server Error` — unexpected server issue

## Ambiguities intentionally left in this spec

Some details are not fully defined on purpose.
Part of the exercise is identifying what additional questions you would ask.
