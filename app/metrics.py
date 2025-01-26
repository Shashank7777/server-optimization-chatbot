import psutil

def get_system_metrics():
    """Collect system performance metrics."""
    metrics = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory()._asdict(),
        "disk_usage": psutil.disk_usage('/')._asdict(),
        "network_io": psutil.net_io_counters()._asdict()
    }
    return metrics
