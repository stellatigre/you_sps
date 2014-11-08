Design Notes
------------

* USPS return label images in PDF or TIFF (googling around indicates PDF was the better choice, so i did that)
* Json responses retain the `RateV4Response` wrapper from the data's XML representation that we get back from USPS.  This can easily be eliminated.
* Currently, the code assumes the existence of /pdfs/ and /json/ directories, since that's the kind of stuff that could/should be handled by a setup / deploy script
