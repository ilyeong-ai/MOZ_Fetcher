from prometheus_client import Counter, Histogram, start_http_server
import time

EVENTS_PROCESSED = Counter('events_processed_total', 'Total number of processed events')
EVENT_PROCESSING_TIME = Histogram('event_processing_seconds', 'Time spent processing events')

def start_metrics_server(port):
    start_http_server(port)

class TimerContextManager:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start
        EVENT_PROCESSING_TIME.observe(self.interval)