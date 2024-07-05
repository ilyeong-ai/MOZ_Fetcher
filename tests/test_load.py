from locust import HttpUser, task, between

class TetherEventUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def fetch_events(self):
        self.client.post("/process-events", json={"from_block": 1, "to_block": 100})

    @task
    def query_graphql(self):
        query = """
        query {
            tetherEvents(fromBlock: 1, toBlock: 100) {
                fromAddress
                toAddress
                value
                blockNumber
                transactionHash
            }
        }
        """
        self.client.post("/graphql", json={"query": query})