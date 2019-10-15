# Log IP GeoInfo

Install and activate Python 3 virtual environment:

    python3 -m venv venv
    source venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Download the current GeoLite2 database, unpack it and copy the file **GeoLite2-City.mmdb** to `databases/`:

    https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz


Run the script with the log file path as argument:

    python log-ip-geoinfo.py path/to/logfile.log
