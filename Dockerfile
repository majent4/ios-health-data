FROM python:3.12.0a7-alpine3.17@sha256:d093b457473827c8debb91f9d0aee743c7f273f3baeef4f0a77b35534c45b1d0 as export

WORKDIR /app/

COPY export.xml export/main.py export/sqlite_database.py export/utils.py export/xml_parser.py ./

RUN python3 main.py export.xml export.db

FROM node:19.7.0-alpine3.16@sha256:36a9713993ecd9c602084f9d3da715626c6354a7d8979bff7ae0d92a75ffe1ab

WORKDIR /app/

COPY --from=export /app/export.db ./

COPY evidence/package.json evidence/package-lock.json ./

COPY evidence/pages ./pages

RUN apk add --no-cache dumb-init=1.2.5-r1 git=2.36.6-r0 && npm i

# https://docs.evidence.dev/cli/#environment-variables

ENV DATABASE=sqlite

ENV SQLITE_FILENAME=export.db

ENTRYPOINT ["dumb-init", "npm", "run", "dev", "--", "--host", "0.0.0.0"]
