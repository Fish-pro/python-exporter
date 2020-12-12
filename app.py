import os
import threading

from flask import Flask, Response
from prometheus_client import generate_latest, ProcessCollector

from apps.metrics.server import Monitor

app = Flask(__name__)


def run():
    print("test")


@app.route('/')
def hello_world():
    threading.Thread(target=run)
    return 'hello world'



@app.route('/metrics')
def metrics():
    g_monitor = Monitor()
    g_monitor.set_prometheus()
    # 通过Metrics接口返回统计结果
    registry = g_monitor.get_prometheus_metrics_info()
    return Response(generate_latest(registry), mimetype="text/plain")


if __name__ == '__main__':
    app.run()
