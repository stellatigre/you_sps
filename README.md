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
`response = requests.post('http://host:port/label', json.dumps(test_label_opts))`
`pprint(response.content)`

currently, this route both saves the PDF image to the server as well as forwarding the base64 representation on to the client.  A link to the PDF image is returned with the response as the "image_url" parameter.
We should decide which we want, if not both.

`/rates`: example data can be found in xml_templates.py -> test_rate_opts

can be used like so:
`response = requests.post('http://host:port/rates', json.dumps(test_rate_opts))`
`pprint(response.content)`
