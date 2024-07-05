import graphene
from app.database import events_collection

class TetherEvent(graphene.ObjectType):
    from_address = graphene.String()
    to_address = graphene.String()
    value = graphene.String()
    block_number = graphene.Int()
    transaction_hash = graphene.String()

class Query(graphene.ObjectType):
    tether_events = graphene.List(TetherEvent, 
                                  from_block=graphene.Int(), 
                                  to_block=graphene.Int())

    def resolve_tether_events(self, info, from_block=None, to_block=None):
        query = {}
        if from_block:
            query['block_number'] = {'$gte': from_block}
        if to_block:
            query.setdefault('block_number', {})['$lte'] = to_block
        
        events = events_collection.find(query)
        return [TetherEvent(
            from_address=event['from'],
            to_address=event['to'],
            value=str(event['value']),
            block_number=event['block_number'],
            transaction_hash=event['transaction_hash']
        ) for event in events]

schema = graphene.Schema(query=Query)