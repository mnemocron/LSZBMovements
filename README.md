# LSZBMovements
Website Scraper for LSZB Airport arrivals/departures Table.
Serves the arrivals/departures Table as a JSON API (files).

---

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![volkswagen status](https://auchenberg.github.io/volkswagen/volkswargen_ci.svg?v=1)](https://github.com/auchenberg/volkswagen)

This script downloads the html table from the LSZB website: [bernairport.ch](https://www.bernairport.ch/en/) and parses it into two `timetable.json` files.


### Usage

Use the `-o` parameter to specify the output directory.

```bash
python3 get-lszb.py -o belp/
```

Outputs: `belp/arrivals.timetable.json` and `belp/departures.timetable.json` 

### Example Output

```json
{
  "data": [
    {
      "flightNo": "NJE794R",
      "airport": "Ljubljana",
      "via": "",
      "scheduledTime": "12:30",
      "estimatedTime": "",
      "gate": "",
      "status": "",
      "privateflight": "Private Flight",
      "direction" : "arrival"
    }
  ]
}
```

---

LICENSE

Apache License 2.0

(c) 2020 Simon Burkhardt



