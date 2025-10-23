# Network Building Module: Cloud Variants (Expansion)

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Overview

**Cloud Variant Cards** extend the Network Building module with advanced cloud deployment options and cloud-native technologies beyond the basic Cloud Workload card in the core deck.

- **Total Cards:** 4 (CLOUD-01 to CLOUD-04)
- **Used In:** Network Building expansion (for cloud-first and advanced deployments)
- **Prerequisite:** Understand ARCH-04 (Cloud Hybrid) or ARCH-05 (Cloud First)
- **Design Philosophy:** Cloud variants offer different trade-offs: cost, complexity, security, scalability

---

## Cloud Variant Cards

### CLOUD-01: Containerized Microservices
**Type:** Cloud-Native Architecture
**Cost:** 6 Budget (container orchestration platform)
**Complexity:** 3/4 (requires Kubernetes expertise)
**Supported Platforms:** AWS ECS, Azure Container Instances, Google Cloud Run, Kubernetes
**Application Type:** Modern cloud-native applications built as multiple small services

**Description:**
Applications broken into microservices running in containers (Docker). Each service is a separate container that can scale independently. Containers are orchestrated by a platform (Kubernetes, Docker Swarm, ECS).

**Key Characteristics:**
- **Services:** Application broken into small, focused services
- **Containers:** Each service runs in a container (isolated environment)
- **Orchestration:** Platform automatically manages container deployment, scaling, and recovery
- **Scalability:** Each service can scale independently based on demand
- **DevOps:** Infrastructure and code are tightly integrated (Infrastructure as Code)
- **Cloud-Native:** Built for cloud (ephemeral resources, auto-scaling, auto-healing)

**Key Advantages:**
- Scalability: Auto-scale individual services based on load
- Resilience: Container failure doesn't affect entire application
- Efficiency: Containers share OS kernel (more efficient than VMs)
- Velocity: Deploy microservices independently (faster development)
- Cost: Pay only for resources used (serverless principles)

**Key Concerns (Security Perspective):**
- Complexity: Many moving parts, many potential attack surfaces
- Container Escape: Attacker in one container might escape to host
- Supply Chain: Container images come from registries (may be compromised)
- Secrets Management: Container needs credentials/API keys (risk of exposure)
- Lateral Movement: Multiple containers in same cluster, network policies must isolate
- Compliance: Tracing data across microservices complicated
- Logging: Distributed across many containers (aggregation required)

**Defense Strategy:**
- **Container Runtime Security:** Monitor and restrict container behavior (Falco, Sysdig)
- **Image Scanning:** Scan images for vulnerabilities before deployment
- **Network Policies:** Kubernetes network policies restrict inter-service communication
- **Pod Security Policies:** Restrict what containers can do (no privileged escalation)
- **Registry Security:** Scan images in registry, require signing
- **Secrets Vault:** Use HashiCorp Vault or cloud native secrets (not environment variables)
- **SIEM Integration:** Aggregate logs from all containers

**Network Interactions:**
- **Works with:** Cloud-native architecture (ARCH-05)
- **Requires:** Container orchestration platform (Kubernetes)
- **Requires:** Container registry (Docker Hub, ECR, ACR, GCR)
- **Requires:** Secrets management (HashiCorp Vault, AWS Secrets Manager)
- **Integrates with:** Microservices architecture (multiple services)

**Incident Response Impact:**
- Container compromise may be isolated (if network policies work)
- Container escape would give attacker access to host
- Supply chain attack on container images affects all deployments
- Distributed nature makes forensics complex
- Log aggregation essential for investigation

**Team Design Validation:**
- ✓ If including microservices: must include container runtime security
- ✓ Must include image scanning + signing
- ✓ Must include network policies
- ✓ Must include secrets management
- ✗ Failure: Hardcoded secrets in containers
- ✗ Failure: No image signing/scanning
- ✗ Failure: No container network policies

---

### CLOUD-02: Serverless/Function-as-a-Service
**Type:** Cloud-Native Compute (Abstracted Infrastructure)
**Cost:** 3 Budget (minimal infrastructure management)
**Complexity:** 2/4 (simple from ops perspective, but different security model)
**Supported Platforms:** AWS Lambda, Azure Functions, Google Cloud Functions, IBM Cloud Functions
**Use Cases:** Event-driven processing, API backends, scheduled jobs, data transformation

**Description:**
Functions deployed to serverless platform. You write code, platform handles scaling, infrastructure, and execution. You pay only for actual execution time (milliseconds).

**Key Characteristics:**
- **No Infrastructure:** You don't manage servers/containers/VMs
- **Event-Driven:** Functions triggered by events (API call, message queue, schedule, etc.)
- **Auto-Scaling:** Automatically scales from zero to thousands of concurrent executions
- **Stateless:** Functions should not maintain state (state in database/message queue)
- **Time-Limited:** Function has timeout (usually 15 minutes max)
- **Cost Model:** Pay per execution millisecond (very cheap if infrequently called)

**Key Advantages:**
- Simplicity: Write code, deploy, done (no servers to manage)
- Cost: Pay only for execution time (not for idle servers)
- Scalability: Automatic scaling without configuration
- Velocity: Rapid deployment cycle (seconds)
- Reduced Attack Surface: No server to compromise (provider manages infrastructure)

**Key Concerns (Security Perspective):**
- Dependency Management: Function depends on libraries (vulnerable packages)
- Secrets in Environment Variables: Function needs credentials (hardcoded or env vars)
- Supply Chain: Libraries may be compromised (dependency attack)
- Monitoring Blind Spot: Functions are ephemeral (logs must be aggregated)
- Cold Start Attacks: Function startup time can leak information
- Privilege Escalation: Function may have overly broad IAM permissions
- Denial of Service: Function can be invoked repeatedly (cost/resource attack)
- Compliance: Difficult to audit function execution (multi-tenant platform)

**Defense Strategy:**
- **Dependency Scanning:** Scan dependencies for vulnerabilities
- **Secrets Management:** Use cloud secrets manager (not environment variables)
- **IAM Least Privilege:** Function has minimum required permissions
- **CloudTrail Logging:** Log all function invocations
- **VPC Integration:** Function connects to VPC if accessing private resources
- **Rate Limiting:** Prevent function invocation DoS
- **Input Validation:** Strict validation of all inputs (injection attacks)
- **Library Pinning:** Pin exact library versions (prevent supply chain attacks)

**Network Interactions:**
- **Works with:** Cloud-first architecture (ARCH-05)
- **Integrates with:** API Gateway (exposes function as HTTP endpoint)
- **Integrates with:** Message Queues (event-driven triggers)
- **Requires:** Secrets Manager (for credentials)
- **Optional:** VPC integration for private resource access

**Incident Response Impact:**
- Function compromise is possible (code vulnerability or dependency)
- Function invocation logs are critical (only audit trail)
- Multi-tenant platform may complicate forensics
- Dependency vulnerability affects all functions using vulnerable library
- Distributed nature makes understanding attack chain difficult

**Team Design Validation:**
- ✓ If including serverless: must include secrets management
- ✓ Must include dependency scanning
- ✓ Must include IAM least privilege configuration
- ✗ Failure: Secrets in environment variables
- ✗ Failure: Overly broad function permissions
- ✗ Failure: No input validation

---

### CLOUD-03: Database-as-a-Service (Managed Database)
**Type:** Cloud-Managed Data Layer
**Cost:** 5 Budget (pay per GB + IO operations)
**Complexity:** 1/4 (cloud provider manages infrastructure)
**Supported Platforms:** AWS RDS, Azure SQL Database, Google Cloud SQL, MongoDB Atlas, DynamoDB
**Database Types:** Relational (SQL Server, PostgreSQL, MySQL, Oracle), NoSQL (MongoDB, DynamoDB, Cassandra)

**Description:**
Database managed entirely by cloud provider. You provision database capacity, cloud provider handles: backups, patching, failover, replication, encryption, monitoring.

**Key Characteristics:**
- **Managed:** Cloud provider manages infrastructure (patches, backups, upgrades)
- **Automated Backup:** Point-in-time recovery (no manual backup configuration)
- **Replication:** Automatic geo-replication for disaster recovery
- **Encryption:** Encryption at rest and in transit (built-in)
- **Scaling:** Can scale storage and compute without downtime
- **Monitoring:** Built-in monitoring and alerting
- **Compliance:** Provider maintains compliance certifications (SOC 2, HIPAA, PCI-DSS)

**Key Advantages:**
- Reliability: Provider manages availability (99.99% SLA typical)
- Security: Provider manages patching and security updates
- Compliance: Provider handles compliance certifications
- Cost: No ops team needed to maintain database
- Disaster Recovery: Automated backups and geo-replication
- Scalability: Transparent scaling without downtime

**Key Concerns (Security Perspective):**
- IAM Configuration: Database access via IAM roles (misconfiguration exposes data)
- Network Exposure: Database may be internet-accessible (must restrict)
- Encryption Keys: Cloud provider manages keys (limited control)
- Audit Logging: Must enable audit logging (not always on by default)
- Data Residency: Where is data stored geographically?
- Backup Security: Backups must be encrypted and access-controlled
- Supply Chain: Vendor is now part of attack surface
- Multi-Tenant: Data may share hardware with other customers (trust model)

**Defense Strategy:**
- **Network Isolation:** Database accessible only from application (not internet)
- **IAM Least Privilege:** Only application has access (not human users)
- **Encryption Keys:** Use customer-managed keys (not provider-managed)
- **Audit Logging:** Enable all audit logging (schema changes, access, queries)
- **Monitoring:** Set up alerting on suspicious queries (large exports, drops, etc.)
- **Backup Encryption:** Verify backups are encrypted
- **Access Control:** Disable public IP, use private endpoints only
- **Secrets Management:** Database credentials in secrets vault (not hardcoded)

**Network Interactions:**
- **Works with:** Cloud-first architecture (ARCH-05) or Cloud Hybrid (ARCH-04)
- **Integrates with:** Application tier (via private endpoint)
- **Requires:** Secrets management (for credentials)
- **Incompatible with:** On-premises applications (latency/connectivity issues)

**Incident Response Impact:**
- Database compromise likely primary attack goal (most valuable data)
- Cloud provider manages baseline security (shifts responsibility model)
- Audit logs are critical evidence (may be only forensics available)
- Backup verification essential (can you restore to pre-attack state?)
- Multi-tenant concerns for sensitive investigations

**Team Design Validation:**
- ✓ If including managed database: must use private endpoints (not public)
- ✓ Must enable audit logging
- ✓ Must use customer-managed encryption keys
- ✓ Must restrict database IAM permissions
- ✗ Failure: Database public IP exposed to internet
- ✗ Failure: Overly broad IAM permissions (anyone can access)
- ✗ Failure: Audit logging disabled

---

### CLOUD-04: Content Delivery Network (CDN)
**Type:** Edge Computing / Performance Enhancement
**Cost:** 4 Budget (pay per GB transferred + requests)
**Complexity:** 2/4 (configuration required, but well-documented)
**Supported Platforms:** CloudFlare, AWS CloudFront, Azure CDN, Google Cloud CDN, Akamai
**Use Cases:** Static assets (images, JS, CSS), web application acceleration, DDoS mitigation

**Description:**
CDN caches content across globally distributed edge servers. When users request content, they get it from nearest edge server (fast). Reduces load on origin server and improves user experience.

**Key Characteristics:**
- **Distributed Caching:** Content cached at 100+ edge locations worldwide
- **Fast Delivery:** Users get content from nearest edge (milliseconds)
- **Origin Protection:** Origin server behind CDN (hides IP, reduces load)
- **DDoS Protection:** CDN absorbs DDoS attacks before reaching origin
- **SSL/TLS Termination:** CDN handles encryption (origin can use HTTP)
- **Rate Limiting:** Can rate-limit requests per IP
- **Security Headers:** Can inject security headers (HSTS, CSP, etc.)

**Key Advantages:**
- Performance: Content delivery 100x faster globally
- DDoS Protection: Built-in DDoS mitigation
- Security: Origin IP hidden, security scanning at edge
- Cost Efficiency: Reduces origin server bandwidth costs
- Geo-Location: Can route users to different content based on location

**Key Concerns (Security Perspective):**
- Cache Poisoning: Attacker poisons CDN cache with malicious content
- Origin Bypass: Attacker finds origin IP, bypasses CDN security
- SSL Stripping: CDN can decrypt traffic (must trust CDN provider)
- Cookie Security: Sensitive cookies may be cached (GDPR/privacy issue)
- Personalization: Cached content loses personalization (may expose user data)
- Configuration Mistakes: Wrong cache settings may cache sensitive content
- Origin Protection: Still need to protect origin server (CDN is not complete solution)
- Bot Attack: Attackers can still target origin through CDN

**Defense Strategy:**
- **Cache Settings:** Do not cache sensitive content (set cache headers)
- **Origin Protection:** Implement Web Application Firewall (WAF) on origin
- **Rate Limiting:** Configure CDN rate limiting rules
- **DDoS Settings:** Enable DDoS protection features
- **SSL Validation:** Verify SSL certificates (prevent MITM)
- **Geoblocking:** Block traffic from unwanted regions (geo-restrictions)
- **Security Headers:** Implement security headers (HSTS, CSP, X-Frame-Options)
- **Origin IP Hiding:** Use origin concealment (hide real IP)
- **Monitoring:** Monitor for suspicious CDN patterns

**Network Interactions:**
- **Works with:** Web application (static assets + dynamic content)
- **Works with:** Cloud Hybrid (ARCH-04) or Cloud First (ARCH-05)
- **Complements:** Web Application Firewall (WAF)
- **Optional with:** Infrastructure (performance enhancement, not required)

**Incident Response Impact:**
- CDN compromise could distribute malware to all users (supply chain attack)
- Cache poisoning affects entire user base
- Origin IP exposure could enable direct attacks on origin server
- CDN logs are evidence (attacker activity visible in CDN analytics)
- DDoS attack visibility (CDN shows attack patterns)

**Team Design Validation:**
- ✓ If including CDN: must configure cache headers correctly
- ✓ Must enable security features (DDoS, WAF, rate limiting)
- ✓ Should hide origin IP
- ✗ Failure: Caching sensitive/personalized content
- ✗ Failure: Disabled security features
- ✗ Failure: Origin IP exposed

---

## Cloud Variants Card Summary

| Card | Technology | Cost | Complexity | Primary Benefit |
|------|-----------|------|-----------|-----------------|
| CLOUD-01 | Microservices | 6 | 3/4 | Scalability & Velocity |
| CLOUD-02 | Serverless | 3 | 2/4 | Simplicity & Cost |
| CLOUD-03 | Managed DB | 5 | 1/4 | Reliability & Compliance |
| CLOUD-04 | CDN | 4 | 2/4 | Performance & DDoS Protection |

---

## Design Philosophy

**Key Principle: Different Cloud Services, Different Security Models**

Each cloud variant represents different architectural choices:
- **Microservices:** Scalability + complexity (many attack surfaces)
- **Serverless:** Simplicity + different threat model (function-level security)
- **Managed Database:** Reliability + shared responsibility (provider + customer)
- **CDN:** Performance + edge computing (distributed security)

Organizations use combinations of these services:
- Serverless functions backed by managed database (simple, scalable, reliable)
- Microservices deployed globally via CDN (scalable, fast, available)
- Mix of serverless and containers (different workloads, different approaches)

---

## Gameplay Impact

### Network Design Flexibility
Cloud variants add flexibility to network design:
- Can build entirely on serverless (very simple, minimal infrastructure)
- Can mix serverless + containers (different workloads)
- Can add CDN for global distribution
- Can use managed database for all data needs

### Cost Considerations
Cloud variants have different cost models:
- **Serverless:** Cheap if used occasionally, expensive if always running
- **Microservices:** Scale-to-zero not available (always running cost)
- **Managed Database:** Scale with usage (can get expensive)
- **CDN:** Cheap for low traffic, expensive for high traffic

### Complexity Trade-offs
Cloud variants trade operational complexity for different concerns:
- **Serverless:** No ops burden, but security mindset different
- **Microservices:** Ops burden (Kubernetes), but powerful scalability
- **Managed Database:** No ops burden, but IAM misconfiguration risk
- **CDN:** Config once, then mostly set-and-forget

---

## When to Use Cloud Variants

### Use in Network Building Expansion if:
- Playing with experienced teams
- Want to explore cloud-native architectures
- Want to teach different cloud service trade-offs
- Have time for complex cloud design discussions

### Skip Cloud Variants if:
- Playing with beginners (too much cloud complexity)
- Want simpler network design
- Not focused on cloud (still on-premises focused)
- Limited play time

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Color-code by deployment type:
   - **Blue (Containers):** CLOUD-01
   - **Green (Serverless):** CLOUD-02
   - **Purple (Data):** CLOUD-03
   - **Orange (Delivery):** CLOUD-04
3. Include cloud provider logos if desired (AWS, Azure, GCP)
4. Cut along dotted lines
5. Create a "Cloud Architecture Reference Card" comparing services

---

## Integration with Core Cloud Cards

### Cloud Core Deck (from core-deck/architecture-cards.md)
- **ARCH-04 (Cloud Hybrid):** Can use any of these cloud variants
- **ARCH-05 (Cloud First):** Typically uses combination of these variants
- **SRV-08 (Cloud Workload):** Can be powered by any of these variants

### Recommended Combinations
- **Serverless + Managed DB + CDN:** Ideal for web applications (cheap, scalable, fast)
- **Microservices + Managed DB + CDN:** Ideal for complex apps (powerful, scales well)
- **Managed DB only:** Simplest cloud setup (just move database to cloud)
- **All four:** Bleeding-edge cloud-native (most complex, most powerful)

---

## Possible Future Expansions

**Additional Cloud Variant Cards:**
- CLOUD-05: Machine Learning Platform (ML training/inference)
- CLOUD-06: Event Streaming (Kafka, pub/sub architectures)
- CLOUD-07: Search & Analytics (Elasticsearch, BigQuery)
- CLOUD-08: API Gateway (API management and rate limiting)
- CLOUD-09: Message Queue (async processing, event-driven)
- CLOUD-10: Infrastructure as Code Platform (automated deployment)

---

*Network Building Module: Cloud Variants (Expansion)*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
