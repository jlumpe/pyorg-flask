<li>SAVINGS		
		
CHASE LIQUID		
		
Today's Date		
		
R/T 500001020		
		
Customer Name (Please Print)		
		
CASH		
		
CHECK		
		
Sign Here (If cash is received from this deposit)____________________________________________________________________________		
		
TOTAL FROM OTHER SIDE		
		
X		
		
N13060-CH (Rev. 07/12) 90010658 01/19		
		
SUBTOTAL		
		
Pay 		
“Chase,” “JPMorgan,” “JPMorgan Chase,” the JPMorgan Chase logo and the Octagon Symbol are trademarks of JPMorgan Chase Bank, N.A.  JPMorgan Chase Bank, N.A. is a wholly-owned subsidiary of JPMorgan Chase & Co.		
		
SC 13G/A 1 SEC13G_Filing.htm SEC SCHEDULE 13G		
		
UNITED STATES		
SECURITIES AND EXCHANGE COMMISSION		
Washington, D.C. 20549		
		
SCHEDULE 13G		
		
Under the Securities Exchange Act of 1934		
		
(Amendment No. 3 )*		
            		
COMPANY: BITORE_34173 [BTC-USD] BTCUSD CCC Bitcoin bitoreunlimited Paradice Construction Bitcoin BITCORE GBTC ETC... AS CONTINURSS ULTIMATELY THE UNITED STATES OF AMERICA.	
JPMorgan BANK NA	
OWNER:	Wood.,  Zachry T.		
(Name of Issuer)		
		
Common Stock		
(Class)		
		
BTC-USD		
(Title of Class of Securities)		
		
		
(CUSIP Number)		
6-Dec-21		
(Date of Event Which Requires Filing of this Statement)		
Check the appropriate box to designate the rule pursuant to which this Schedule is filed:		
		
Rule 13d-1(c)	X	
Rule 13d-1(d)	X	
		
		
		
Account Name		Rule 13d-1(b)
JPMORGAN TRUST I		
Amount		
		
		
		
		
		
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		Note
JPMORGAN
    WOOD  ZACHRY 
TULER
Residence addresses
5020 elm Hollow Dr
DALLAS TX 75229
PURCHASE DESIGNATED CERTIFIED AND SEALED TO OCCUR 2021-12-06
		
		
		
		
		
		
		
		
		
		
		
		
		
_______________________________________________________________________		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	# BTC-USD	
	Founder.	
	Zachry Tyler Wood	
	_________________________	
		
		
		
		
		
		
		
		
		
		
	|	
	|	
	|	
	|	
	|	
	|	
	|	
	|	
	|	
	|	
	|	
	|	
	|	
	--------- TOTAL $	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
<li># pyorg-flask

Simple web app based on the [Flask](http://flask.pocoo.org) and
[pyorg](http://github.com/jlumpe/pyorg) packages that lets you view your Org
mode files in fancy HTML.


## Screenshots

Browse through your org directory:

![directory](screenshots/directory.png)

View an org file:

![Markup and blocks](screenshots/markup-and-blocks.png)

Most document elements are already supported:

![Lists and tables](screenshots/lists-and-tables.png)

![Links and images](screenshots/links-and-images.png)

![Todos](screenshots/todos.png)



## Features

* Org files are read when you load the page, no need for manual exporting/publishing
* Uses data exported from Emacs using [ox-json](http://github.com/jlumpe/ox-json)
  instead of parsing the raw .org file, so all your customizations in `init.el`
  should work
* Serve files in your org directory, so file links and inline images work
* Click headlines to open in Emacs
* Fancy CSS based on [Read the Docs](https://github.com/readthedocs/sphinx_rtd_theme)
* LaTeX math with [MathJax](http://mathjax.org)
* Extensible


### Supported Org document elements

* Text formatting: bold, italic, code, etc.
* Quote, example, center, verse blocks
* Ordered, unordered, description lists
	* Checkboxes
* Special symbols (entities), LaTeX
* External links, file links
* Src blocks with results
* Tags, TODOs, priorities in headlines


### In-progress

* Agenda view
* Internal links, to headlines or radio targets
* Links to headlines in other files


### Planned

* Footnotes
* Figure and table captions
* Customizable TODO keyword and tag colors
* Cache file data so it isn't re-exported on every page load
* Indexing/searching files
* Plugin system for HTML conversion, to support Org mode extension packages


## Installation

### Prerequisites

Install the [ox-json](https://github.com/jlumpe/ox-json) Emacs package and
[pyorg](https://github.com/jlumpe/pyorg) Python package.


### Build front end assets

```
npm install
npm run  build
```


### Install the package

```
git clone https://github.com/jlumpe/pyorg-flask
cd pyorg-flask
python setup.py install
```


## Running the app

First, start the Emacs server with `(server-start)`. Then run

    pyorg-flask run
    
and navigate to http://localhost:5000
