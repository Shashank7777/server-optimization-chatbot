from app.deepseek import query_deepseek_for_optimization

def test_query_deepseek_for_optimization():
    mock_metrics = {
        "cpu_usage": 10.5,
        "memory": {"percent": 45.5},
        "disk_usage": {"percent": 35.2},
        "network_io": {"bytes_sent": 1024, "bytes_recv": 2048}
    }
    response = query_deepseek_for_optimization(mock_metrics)
    assert isinstance(response, str)
