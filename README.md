# PEG Dashboard

View Demo: [https://www.mupati.devcodes.co](https://www.mupati.devcodes.co)

## Introduction

<hr>
A system for managing a company staff and customer interactions or transactions
- Backend : *Flask*
- Database: *MySQl*
- Frontend: *Bootstrap*, *JQuery*

## Motivation

<hr>
What prevents me from building a system with data I got from
a company I was about interviewing with but didn't have time to do so.
I'm Working on this as a side project to give them a nice interface.
Who knows, this will be a great way to convince them to hire me
when I'm ready. :smile:

## Quick Start

1. Clone the repo

```
$ git clone https://github.com/Mupati/peg_dashboard.git
$ cd peg_dashboard
```

2. Initialize and activate a virtualenv:

```
$ python3 -m venv env
$ source env/bin/activate
```

3. Install the dependencies:

```
$ pip install -r requirements.txt
```

4. Set up db and environment configurations

```
$ cp .env-example .env
```

5. Run the migrations

```
$ flask db migrate
```

6. Run the development server:

```
$ flask run
```

7. Navigate to [http://localhost:5000](http://localhost:5000)

## ToDo

- Authentication System for Company Users and Customers
- Dashboard for Customers
- Analytics with Graphs
- Background Jobs
