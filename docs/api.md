# API Documentation

## Endpoints

### POST /process-events

Process Tether transfer events for a given block range.

**Parameters:**
- `from_block`: Integer
- `to_block`: Integer

**Response:**
```json
{
  "status": "success"
}