SC DEPOSIT 1 SECDEPOSIT_Filing.html SEC SCHEDULE DEPOSIT		
UNITED STATES		
SECURITIES AND EXCHANGE COMMISSION		
Washington, D.C. 20549		
SCHEDULE 3-34173
Under the Securities Exchange Act of 1934		
(Amendment No. 3 )*		
COMPANY: BITORE_34173 [BTC-USD] BTCUSD CCC Bitcoin bitoreunlimited Paradice Construction Bitcoin BITCORE GBTC ETC... AS CONTINURSS ULTIMATELY THE UNITED STATES OF AMERICA.	
JPMorgan BANK NA	
OWNER:	Wood.,  Zachry T.		
(Name of Issuer)		
DIRECT: DEPOSIT
DEPOSIT: AMOUNT
AMOUNT: $828165621475.00.00 
NAME: JPMOGAN TRUST I
ACCOUNT HOLDER: Parent
Parent: United States Department of the Treasury
BENEFICIARY; ZACHRY TYLER WOOD 
in personal saving account 0001718745-20-0386 
Series: S000002965
MEMO: PUCHASE FOR ZACHRY WOOD
SAVINGS		
CHASE LIQUID		
Today's Date		
R/T 500001020		
Customer Name (SECURITIES AND EXCHANNGE Commission)
Customer Name(The Department of the Treasury)
Customer name(		
CASH		
Registration No. 333-34173-3172
CHECK 3
ID 3172		
Sign Here (If cash is received from this deposit)____<sign_FORM>________________________________________________________________________		
TOTAL FROM OTHER SIDE		
X_$19500000.00_
N13060-CH (Rev. 07/12) 90010658 01/19 
R/T 500001020 90010658
</focus>
1122333:|-||'500001020||'-:|90010658:|
</R/T>
Purchase:
Register:
Checkout:
1. 
-SUBTOTAL: $ 19500000.00USD
"Payor": "Zachry Tyler Wood'"''©®™“2005Chase,” “JPMorgan,” “JPMorgan Chase,” the JPMorgan Chase logo and the Octagon Symbol are trademarks of JPMorgan Chase Bank, N.A.  JPMorgan Chase Bank, N.A. is a wholly-owned subsidiary of JPMorgan Chase & Co.©®™2005	
SC DEPOSIT 1 SECDEPOSIT_Filing.html SEC SCHEDULE DEPOSIT		
UNITED STATES		
SECURITIES AND EXCHANGE COMMISSION		
Washington, D.C. 20549		
		
SCHEDULE 3-
		
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
TYLER
ACH:
AMOUNT: $ 19500000.00USD
Focus: 0001718745&20&0386&000000000
Paid to the order of: ZILLOW MARKET GROUP
Memo: - AQUISITION
address:5020 elm Hollow Dr DALLAS TX 75229
PURCHASE DESIGNATED ADDRESS LISTED ABOVE 
FILE NO. 333-34173 ID 3172
CERTIFICATE: enabled
SEAL: enabled
Date: 2021-12-06
Run: R/T(021000021)
response: 200 OK
		
		
		
		
		
		
		
		
		
		
		
		
		
_______________________________________________________________________		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
[bitcoin]
[BITORE_34173]
[BTC-USD] 
[BTCUSD CCC]
Founder.		
JPMORGAN CHASE & Co.,
CHASE
JPMORGAN BANK NA
Morgan Stanley Smith & Barney 
Investment Management Holdings Agencies 
Owner
signed on 07/17/2005 17:00:00 CENTAL STANDARD TIME
Zachry_Tyler_Wood
DOB: 10-15-1994
SSID: ***-**-1725
		
		
		
		
		
		
		
		
		
		
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
	Check out in the amount of:_$1.00USD_paod to the order of 	
	--------- TOTAL $	
		
		
		
		
		
		
		
		
		
		
		
		
		
For Institutional Investor Use Only:' O.S.'_Recieved_11/15/2021
		
<li>
# pyorg-flask

Simple web app based on the [Flask](http://flask.pocoo.org) and
[pyorg](http://github.com/jlumpe/pyorg) packages that lets you view your Org
mode files in fancy HTML.


## Screenshots

Browse through your org directory:

![directory](screenshots/directory.png)

View an org file:

'!'[Markup' and' blocks']'('screenshots'/markup'-and'-blocks.png)

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
