"""
Cloud Resource Monitor - Research Project
Author: Pankaj Kumar
Description: A Python-based cloud resource monitoring and cost optimization tool
             that simulates AWS resource tracking and analysis.
"""

import json
import random
import datetime
from typing import Dict, List

# ─── Simulated Cloud Resource Data ───────────────────────────────────────────

def generate_ec2_instances() -> List[Dict]:
    """Simulate AWS EC2 instance data."""
    instance_types = ["t2.micro", "t2.small", "t3.medium", "m5.large", "c5.xlarge"]
    regions = ["us-east-1", "us-west-2", "ap-south-1", "eu-west-1"]
    states = ["running", "running", "running", "stopped", "idle"]

    instances = []
    for i in range(1, 8):
        cpu = random.randint(2, 95)
        instances.append({
            "instance_id": f"i-0{random.randint(1000000, 9999999)}abcd",
            "type": random.choice(instance_types),
            "region": random.choice(regions),
            "state": random.choice(states),
            "cpu_utilization": cpu,
            "monthly_cost_usd": round(random.uniform(8.5, 180.0), 2),
            "is_underutilized": cpu < 20
        })
    return instances


def generate_s3_buckets() -> List[Dict]:
    """Simulate AWS S3 bucket data."""
    bucket_names = [
        "project-data-bucket", "backup-storage", "logs-archive",
        "ml-datasets", "static-assets", "research-outputs"
    ]
    return [
        {
            "bucket_name": name,
            "size_gb": round(random.uniform(0.5, 500.0), 2),
            "object_count": random.randint(10, 50000),
            "monthly_cost_usd": round(random.uniform(0.02, 12.0), 2),
            "public_access": random.choice([True, False, False, False])
        }
        for name in bucket_names
    ]


# ─── Analysis Functions ───────────────────────────────────────────────────────

def analyze_cost(instances: List[Dict], buckets: List[Dict]) -> Dict:
    """Calculate total cloud spending and identify waste."""
    ec2_cost = sum(i["monthly_cost_usd"] for i in instances)
    s3_cost = sum(b["monthly_cost_usd"] for b in buckets)
    total = ec2_cost + s3_cost

    wasted = sum(
        i["monthly_cost_usd"] for i in instances
        if i["is_underutilized"] or i["state"] in ["stopped", "idle"]
    )

    return {
        "ec2_monthly_cost": round(ec2_cost, 2),
        "s3_monthly_cost": round(s3_cost, 2),
        "total_monthly_cost": round(total, 2),
        "estimated_waste_usd": round(wasted, 2),
        "savings_potential_percent": round((wasted / total) * 100, 1) if total > 0 else 0
    }


def security_audit(buckets: List[Dict]) -> List[str]:
    """Check for security issues in cloud resources."""
    alerts = []
    for b in buckets:
        if b["public_access"]:
            alerts.append(f"⚠️  SECURITY ALERT: Bucket '{b['bucket_name']}' has PUBLIC access enabled!")
    if not alerts:
        alerts.append("✅ No public S3 buckets detected. Good security posture!")
    return alerts


def recommendations(instances: List[Dict]) -> List[str]:
    """Generate optimization recommendations."""
    recs = []
    for i in instances:
        if i["state"] == "stopped":
            recs.append(f"💡 Instance {i['instance_id']} is STOPPED — consider terminating to save ${i['monthly_cost_usd']}/month.")
        elif i["is_underutilized"]:
            recs.append(f"📉 Instance {i['instance_id']} CPU at {i['cpu_utilization']}% — downsize from {i['type']} to save cost.")
        elif i["state"] == "idle":
            recs.append(f"⏸️  Instance {i['instance_id']} is IDLE — schedule auto-shutdown during off-hours.")
    if not recs:
        recs.append("✅ All instances appear optimally utilized.")
    return recs


# ─── Report Generator ─────────────────────────────────────────────────────────

def generate_report(instances: List[Dict], buckets: List[Dict]) -> str:
    """Generate a full cloud health report."""
    cost = analyze_cost(instances, buckets)
    security = security_audit(buckets)
    recs = recommendations(instances)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""
╔══════════════════════════════════════════════════════╗
║         CLOUD RESOURCE MONITOR - HEALTH REPORT       ║
╚══════════════════════════════════════════════════════╝
  Generated: {timestamp}
  Author   : Pankaj Kumar | Team: mr-robot

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📊 COST ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  EC2 Instances Cost  : ${cost['ec2_monthly_cost']}/month
  S3 Storage Cost     : ${cost['s3_monthly_cost']}/month
  Total Monthly Cost  : ${cost['total_monthly_cost']}/month
  Estimated Waste     : ${cost['estimated_waste_usd']}/month
  Savings Potential   : {cost['savings_potential_percent']}%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🔒 SECURITY AUDIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for alert in security:
        report += f"  {alert}\n"

    report += """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  💡 OPTIMIZATION RECOMMENDATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for rec in recs:
        report += f"  {rec}\n"

    report += """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✅ Report complete. Implement recommendations to
     optimize cloud spend and improve security.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    return report


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("🔄 Fetching cloud resource data...\n")
    instances = generate_ec2_instances()
    buckets = generate_s3_buckets()

    print(f"  Found {len(instances)} EC2 instances")
    print(f"  Found {len(buckets)} S3 buckets\n")

    report = generate_report(instances, buckets)
    print(report)

    # Save report as JSON
    output = {
        "timestamp": datetime.datetime.now().isoformat(),
        "ec2_instances": instances,
        "s3_buckets": buckets,
        "cost_analysis": analyze_cost(instances, buckets),
        "security_alerts": security_audit(buckets),
        "recommendations": recommendations(instances)
    }
    with open("cloud_report.json", "w") as f:
        json.dump(output, f, indent=2)
    print("📁 Full report saved to cloud_report.json")
