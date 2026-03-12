# Task 2 — Example Answers

## 1. Test cases

1. Create job with all valid fields and expect 201.
2. Create job with only required fields and expect 201.
3. Omit `user_id` and expect validation error.
4. Omit `text` and expect validation error.
5. Send `user_id` as a string and expect validation error.
6. Send `user_id` as 0 and expect validation error.
7. Send `text` as blank spaces and expect validation error.
8. Send `text` with exactly 5000 characters and verify accepted.
9. Send `text` with 5001 characters and expect rejection.
10. Send unsupported `voice` value and expect validation error.
11. Send `speed` below 0.5 and expect validation error.
12. Send `speed` above 2.0 and expect validation error.
13. Send unsupported `format` and expect validation error.
14. Send malformed JSON and expect 400.
15. Send request without auth and expect 401.
16. Send request with wrong content type and expect 415.
17. Send too many requests quickly and expect 429.
18. Retry same request and check whether duplicate handling is defined.

## 2. Expected status codes

- 201 Created for successful job creation
- 400 Bad Request for malformed JSON
- 401 Unauthorized for missing/invalid auth
- 403 Forbidden for insufficient permissions
- 413 Payload Too Large for oversized text payloads, if implemented that way
- 415 Unsupported Media Type for invalid content type
- 422 Unprocessable Entity for validation failures
- 429 Too Many Requests for throttling
- 500 Internal Server Error for unexpected server issues

## 3. Risks / ambiguities in the spec

1. The maximum text length is defined, but it is unclear whether 5000 is inclusive.
2. It is unclear whether duplicate requests should create duplicate jobs or return conflict.
3. The authentication method is not defined.
4. Error response schema is not defined consistently.
5. It is unclear whether `speed` accepts integers only or any decimal value in range.
6. The spec does not say whether trailing spaces in `text` are valid or trimmed.
7. Rate limit rules are not defined.

## 4. Test data preparation

I would prepare valid and invalid user IDs, short text, max-length text, over-limit text, blank text, unsupported enum values, boundary `speed` values like 0.5 and 2.0, and out-of-range values like 0.49 and 2.01. I would also prepare auth variations and malformed JSON bodies.

## 5. Bug reports

### Bug report 1
- Title: API creates audio job when required field `text` is missing
- Preconditions: Valid authenticated user and endpoint available
- Steps to reproduce:
  1. Send POST `/v1/audio/jobs`
  2. Use body without `text`
  3. Observe response
- Expected result: Request is rejected with validation error, for example 422, indicating `text` is required
- Actual result: API returns 201 Created and queues a job
- Severity: High
- Priority: High

### Bug report 2
- Title: Unsupported `voice` value `robot` is accepted by audio job creation API
- Preconditions: Valid authenticated user and endpoint available
- Steps to reproduce:
  1. Send POST `/v1/audio/jobs`
  2. Use `voice: robot`
  3. Observe response
- Expected result: Request is rejected because `voice` must be one of `alloy`, `nova`, or `echo`
- Actual result: API returns 201 Created
- Severity: Medium
- Priority: High

### Bug report 3
- Title: API returns 200 OK with error body when text exceeds maximum length
- Preconditions: Valid authenticated user and endpoint available
- Steps to reproduce:
  1. Send POST `/v1/audio/jobs`
  2. Use `text` longer than 5000 characters
  3. Observe response
- Expected result: API returns a validation-related status such as 413 or 422 with a consistent error schema
- Actual result: API returns 200 OK with `{ "error": "text too long" }`
- Severity: Medium
- Priority: Medium
