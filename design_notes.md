Design Notes
------------

* USPS return label images in PDF or TIFF (googling around indicates PDF was the better choice, so i did that)
* Database implementation is naive at the moment, and questions of session creation / scope and such should be more closely considered if this is to be used in production - for now, it immediately commits and flushes all additions to the session for immediate feedback.  Undoubtedly, there is a more efficient way.
* On the note of the database, currently it's just setup to store responses, not requests.  In addition, DB entries for /labels are on the "to do" list
* possible uses for database portion : keep track of customer history or to analyze trends in usage
* Json responses retain the `RateV4Response` wrapper from the data's XML representation that we get back from USPS.  This can easily be eliminated.
* JSON serialization has been left in the Flask portion of the app, service.py, for the most part - it makes sense to me to have that be in the same area as HTTP operations.
* Does not check for incorrect or too large package dimensions, as USPS's api is happy to provide an error for that, which it will pass back to you in JSON.
* Currently, the code assumes the existence of /pdfs/ and /json/ directories to save files, since that's the kind of stuff that could/should be handled by a setup / deploy script
