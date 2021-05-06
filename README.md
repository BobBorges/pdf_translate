# Pdf_translate
This is a commandline tool to translate pdf documents.

It generates a text rendering of the original pdf and a translation text. Some punctuation marks are stripped from the text before translating.

Pdf_trans is not memory efficient, but it should be fine for shorter documents. Honestly, the whole thing should be rewritten, but I wrote it quick and use it a lot.

## Use

* clone repo
* chmod +X pdf_trans.sh
* call

	`./pdf_trans.sh pdf-file.pdf src-langauge dest-language`
	
e.g. to translate myfile.pdf from English to Polish

	./pdf_trans.sh myfile.pdf en pl

If your pdf file name has spaces, you should rename it. Or call the script with single quotes around the file name.

For power users: set a Bash alias to the script and call it quickly from anywhere in your system.

## Dependencies

* Python 3.6+
	- tika
	- google-trans-new
	
`pip` install `tika` and `google-trans-new` before running the script.