# you-sps
## a Python3 JSON wrapper for USPS' rate & label APIs

### Dependencies
* SQLAlchemy + psycopg2 (other DB drivers can be used, theoretically)
* Flask 
* Requests 
* xmltodict 
* simplejson (json is used as a fallback but simplejson is preferred)



routes
======
`/label`: example data structure expected can be found in xml_templates.py -> test_label_opts

can be used like so:
`requests.post('http://host:port/label', json.dumps(test_label_opts))`

`/rates`: example data can be found in xml_templates.py -> test_rate_opts

can be used like so:
`requests.post('http://host:port/rates', json.dumps(test_rate_opts))`
