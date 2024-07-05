7. `docs/architecture.md`:

```markdown
# System Architecture

## Components

1. **FastAPI Application**: Main application server
2. **MongoDB**: Primary database for storing processed events
3. **Redis**: Caching layer for quick access to recent events
4. **RabbitMQ**: Message queue for handling event processing tasks
5. **Prometheus**: Metrics collection and monitoring
6. **Sentry**: Error tracking and performance monitoring

## Data Flow

1. User requests event processing via API
2. Application fetches events from Ethereum blockchain
3. Events are stored in MongoDB and cached in Redis
4. Event processing tasks are queued in RabbitMQ
5. Worker processes events from RabbitMQ queue
6. Processed events are available via GraphQL API

## Scaling Strategy

- Horizontal scaling of FastAPI application
- Sharding of MongoDB for improved read/write performance
- Redis cluster for distributed caching
- RabbitMQ cluster for high availability and throughput

## Backup and Recovery

- Daily automated backups of MongoDB, Redis, and RabbitMQ
- Backup files stored in secure off-site location
- Regular disaster recovery drills

## Security Measures

- JWT authentication for API access
- Rate limiting to prevent abuse
- Regular security audits and penetration testing
- Encryption of sensitive data at rest and in transit