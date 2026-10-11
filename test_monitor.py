"""
Unit Tests for Cloud Resource Monitor
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from cloud_monitor import (
    generate_ec2_instances,
    generate_s3_buckets,
    analyze_cost,
    security_audit,
    recommendations
)

def test_ec2_instances_generated():
    instances = generate_ec2_instances()
    assert len(instances) > 0
    for i in instances:
        assert "instance_id" in i
        assert "cpu_utilization" in i
        assert 0 <= i["cpu_utilization"] <= 100
    print("✅ EC2 instance generation test passed")

def test_s3_buckets_generated():
    buckets = generate_s3_buckets()
    assert len(buckets) > 0
    for b in buckets:
        assert "bucket_name" in b
        assert "size_gb" in b
    print("✅ S3 bucket generation test passed")

def test_cost_analysis():
    instances = generate_ec2_instances()
    buckets = generate_s3_buckets()
    cost = analyze_cost(instances, buckets)
    assert cost["total_monthly_cost"] > 0
    assert cost["ec2_monthly_cost"] >= 0
    assert cost["s3_monthly_cost"] >= 0
    print("✅ Cost analysis test passed")

def test_security_audit():
    buckets = generate_s3_buckets()
    alerts = security_audit(buckets)
    assert isinstance(alerts, list)
    assert len(alerts) > 0
    print("✅ Security audit test passed")

def test_recommendations():
    instances = generate_ec2_instances()
    recs = recommendations(instances)
    assert isinstance(recs, list)
    print("✅ Recommendations test passed")

if __name__ == "__main__":
    print("🧪 Running tests...\n")
    test_ec2_instances_generated()
    test_s3_buckets_generated()
    test_cost_analysis()
    test_security_audit()
    test_recommendations()
    print("\n🎉 All tests passed!")
