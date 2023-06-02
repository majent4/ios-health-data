FROM python:3.12.0a7-alpine3.17@sha256:d093b457473827c8debb91f9d0aee743c7f273f3baeef4f0a77b35534c45b1d0

WORKDIR /app/

COPY export.xml export/csv_reader.py export/main.py export/sqlite_database.py export/utils.py export/xml_parser.py ./

RUN python3 main.py export.xml export.db
