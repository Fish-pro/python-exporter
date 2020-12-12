# encoding: utf-8
import os
import random

from prometheus_client import Counter, Gauge, Summary, Histogram, ProcessCollector
from prometheus_client.core import CollectorRegistry


class Monitor:
    def __init__(self):
        self.collector_registry = CollectorRegistry(auto_describe=True)

        self.summary = Summary(name="summary_test",
                               documentation="test in summary",
                               labelnames=("test",),
                               registry=self.collector_registry)

        self.gauge = Gauge(name="gauge_test",
                           documentation="test in gauge",
                           labelnames=("test",),
                           registry=self.collector_registry)

        self.counter = Counter(name="counter_test",
                               documentation="test in counter",
                               labelnames=("test",),
                               registry=self.collector_registry)

        self.histogram = Histogram(name="histogram_test",
                                   documentation="test in histogram",
                                   labelnames=("test",),
                                   registry=self.collector_registry)
        ProcessCollector(namespace="pc", pid=lambda: os.getpid(), registry=self.collector_registry)

    # 获取/metrics结果
    def get_prometheus_metrics_info(self):
        return self.collector_registry

    def set_prometheus(self):
        self.summary.labels("haha").observe(10)
        self.gauge.labels("hehe").set(1)
        self.counter.labels("zeze").inc()
        self.histogram.labels("tete").observe(random.randint(-10, 10))
