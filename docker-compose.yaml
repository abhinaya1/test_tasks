version: "3.8"
services:
  nodejs-app:
    build:
      context: ./node-js-getting-started
      dockerfile: Dockerfile
    ports:
      - 8080:8080
    depends_on:
      - loki
      - promtail
    logging:
      driver: loki
      options:
        loki-url: "http://loki:3100/loki/api/v1/push"
        loki-external-labels: "container_name={{.Name}}"

  loki:
    image: grafana/loki:latest
    ports:
      - 3100:3100
    command: -config.file=/etc/loki/local-config.yaml
    volumes:
      - ./loki-config.yaml:/etc/loki/local-config.yaml

  promtail:
    image: grafana/promtail:latest
    volumes:
      - ./promtail-config.yaml:/etc/promtail/promtail-config.yaml
      - /var/log:/var/log

  grafana:
    image: grafana/grafana:latest
    ports:
      - 3000:3000
    depends_on:
      - loki
    volumes:
      - ./grafana-data:/var/lib/grafana
    environment:
      GF_INSTALL_PLUGINS: "grafana-piechart-panel"
