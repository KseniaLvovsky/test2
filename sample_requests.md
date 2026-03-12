# Sample Requests and Responses

These examples intentionally contain potential inconsistencies.
Use them to identify bugs and write bug reports.

---

## Example 1 — Missing text accepted

### Request
```json
{
  "user_id": 1001,
  "voice": "alloy",
  "speed": 1.0,
  "format": "mp3"
}
```

### Response
**201 Created**
```json
{
  "job_id": "job_10001",
  "status": "queued"
}
```

Potential issue: required field may have been ignored.

---

## Example 2 — Invalid voice returns success

### Request
```json
{
  "user_id": 1002,
  "text": "Test audio",
  "voice": "robot",
  "speed": 1.0,
  "format": "mp3"
}
```

### Response
**201 Created**
```json
{
  "job_id": "job_10002",
  "status": "queued"
}
```

Potential issue: unsupported enum may be accepted.

---

## Example 3 — Over max text gets wrong status code

### Request
A request with text length of 6001 characters.

### Response
**200 OK**
```json
{
  "error": "text too long"
}
```

Potential issue: response code and format may be inconsistent.

---

## Example 4 — Negative speed accepted

### Request
```json
{
  "user_id": 1004,
  "text": "Speed test",
  "voice": "nova",
  "speed": -1,
  "format": "wav"
}
```

### Response
**201 Created**
```json
{
  "job_id": "job_10004",
  "status": "queued"
}
```

Potential issue: invalid numeric range may not be validated.
