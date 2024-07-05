import pytest
from app.blockchain import get_transfer_events

def test_get_transfer_events():
    events = get_transfer_events(12000000, 12000100)
    assert len(events) > 0
    for event in events:
        assert 'args' in event
        assert 'from' in event['args']
        assert 'to' in event['args']
        assert 'value' in event['args']