from app.metrics import get_system_metrics

def test_get_system_metrics():
    metrics = get_system_metrics()
    assert "cpu_usage" in metrics
    assert "memory" in metrics
    assert "disk_usage" in metrics
    assert "network_io" in metrics
