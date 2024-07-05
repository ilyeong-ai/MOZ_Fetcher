from fastapi import FastAPI, Depends
from starlette.graphql import GraphQLApp
from app.schema import schema
from app.event_processor import process_events
import sentry_sdk
from app.config import SENTRY_DSN, PROMETHEUS_PORT
from app.security import get_current_user
from app.monitoring import start_metrics_server
from app.error_handler import custom_exception_handler, general_exception_handler, CustomException

sentry_sdk.init(dsn=SENTRY_DSN)

app = FastAPI()

app.add_exception_handler(CustomException, custom_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

app.add_route("/graphql", GraphQLApp(schema=schema))

@app.on_event("startup")
async def startup_event():
    start_metrics_server(PROMETHEUS_PORT)

@app.post("/process-events")
async def process_events_endpoint(from_block: int, to_block: int, current_user: dict = Depends(get_current_user)):
    process_events(from_block, to_block)
    return {"status": "success"}