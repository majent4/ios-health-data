## [ios-health-data](https://github.com/majent4/ios-health-data)
Create charts from [Health](https://www.apple.com/ios/health) data using [Evidence](https://evidence.dev) framework and its [components](https://docs.evidence.dev/components/all-components) with SQL and markdown.

## Usage

### Export your Health data
Follow the [instructions](https://support.apple.com/guide/iphone/share-your-health-data-iph5ede58c3d/ios) to export you Health data in XML format and move the file to the root directory.

### Start the server on your machine
1. Import the XML data into a SQLite database:
```
python3 export/main.py export.xml export.db
```
2. Install the dependencies and start the server:
```
cd evidence && npm i && export DATABASE=sqlite && export SQLITE_FILENAME=../export.db && npm run dev -- --host 0.0.0.0
```

### Import the XML data and start the server, inside a container
```
docker compose up
```
