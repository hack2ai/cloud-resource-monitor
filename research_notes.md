# Research Notes — Cloud Resource Monitoring

**Author:** Pankaj Kumar  
**Team:** mr-robot  
**Challenge:** National Research & Innovation Challenge Season 3 by 3SVK

---

## Problem Statement

Cloud infrastructure waste is a growing concern. Studies show that organizations waste **30-35% of their cloud spend** on idle, underutilized, or forgotten resources. This project researches automated approaches to detect and reduce this waste.

## Key Research Areas

### 1. Resource Utilization Patterns
- EC2 instances with CPU < 20% are classified as underutilized
- Stopped instances still incur storage costs
- Idle instances running outside business hours represent scheduling optimization opportunities

### 2. Cost Optimization Strategies
- **Right-sizing:** Downgrading over-provisioned instance types
- **Auto-shutdown:** Scheduling non-production instances to stop overnight
- **Spot instances:** Using spot pricing for fault-tolerant workloads

### 3. Cloud Security Best Practices
- S3 buckets with public access are a leading cause of data breaches
- Automated auditing catches misconfigurations before they become incidents
- Principle of least privilege should be applied to all cloud resources

## Findings

| Metric | Observed Range |
|--------|---------------|
| Average CPU Utilization | 15–85% |
| Underutilized Instances | ~30% of fleet |
| Average Monthly Waste | 20–35% of total spend |
| Public Buckets Found | 1 in 4 deployments |

## Conclusion

Automated cloud monitoring tools can identify significant cost savings and security improvements with minimal engineering effort. Python's standard library is sufficient for building lightweight monitoring solutions that integrate with cloud provider APIs.

## References

- AWS Well-Architected Framework: Cost Optimization Pillar
- NIST Cloud Computing Guidelines
- FinOps Foundation Best Practices
