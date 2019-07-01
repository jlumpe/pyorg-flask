# pyorg-flask
Flask app for pyorg package


## Installation

### Prerequisites

Install the [org-json](github.com/jlumpe/org-json) Emacs package and [pyorg](github.com/jlumpe/pyorg) Python package.

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


# Running the app

First, start the Emacs server with `(server-start)`. Then run

    pyorg-flask run
    
and navigate to http://localhost:5000
