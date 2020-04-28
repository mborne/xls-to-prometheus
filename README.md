# xls-to-prometheus

Conversion d'un tableau de documentation de sonde en configuration prometheus.

## Installation

```bash
pip3 install pyexcel --user
pip3 install jinja2 --user
```

## Utilisation

```bash
python3 main.py sample/qtw.ods > sample/qtw.yml
```

## Intégration dans prometheus

* `cp sample/qtw.yml /etc/prometheus/conf.d/qtw.yml`
* /etc/prometheus/prometheus.yml

```yaml
  - job_name: qtw
    metrics_path: /probe
    scrape_interval: 15s
    params:
      module: [http_2xx]
    file_sd_configs:
      - files:
        - '/etc/prometheus/conf.d/qtw.yml'
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: blackbox-exporter:9115
```
