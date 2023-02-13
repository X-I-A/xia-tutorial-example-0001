# X-I-A Tutorial - Example 0001 - Data Puller
## Getting Started

Welcome to XIA API tutorial!

The goal of this tutorial is to quickly show you how to build a complex application by using X-I-A API framework. 
This framework is microservice based in order to get a fast learning curve for developers and AI.

## How to use this tutorial

Each tutorial is ended by a series number like 01-02-03. The longer the series is, the more advanced topic is discussed.
It will be better to finish basic tutorial before going through advanced ones. Each tutorial has example code. 
Installation instruction could be found at tutorial/install.md.

## Introduction

Data model engine maps the data of data model level to persistent level. 
If considering data as human being, this mapping is like an address book.

The engine level has three main storage features:
* Data redundancy: Each data could be stored in different engines.
* Data cataloging: Each engine could hold a part of data model. (Part of fields)
* Data scoping: Each engine could hold a subset of data model. (Field value filters)

Using purchase order data model of a worldwide sale system as example:
* Only **one purchase order data model** will be defined
* Each country / region could have their own data cataloging saved in local transactional engine, which could base
on different databases.
* All data are real-timely replicated to several engines:
    * Worldwide/Regional OLAP engine with desired data scope and only analytic related fields.
    * Worldwide transactional engine with full scope, full catalog with data expiration*, ideally a document database such as MongoDB or Google Firestore
    * Worldwide big data engine with full scope and full catalog.
    * Worldwide time series database with real-time dashboard related fields.

*) Data expiration is not considered as part of data model and should be implemented directly in database level

All these are supported by the engine level implementation. 

When an api call applies to a data model, the data redundancy allow the data model to choose the best engine.

## Let's start !
### Your first persistence data model in 2 minutes

Data model defined in tutorial 01 are all saved in the memory. In this tutorial, you will be able to download the 
database after inputs. 

Please clone and deploy the example code (see [installation guide](tutorial/install.md) for instruction).

Or just visiting the already deployed [online version](https://xia-tutorial-api-02-srspyyjtqa-ew.a.run.app/order)
Once some order has been created, [database](https://xia-tutorial-api-02-srspyyjtqa-ew.a.run.app/static/db.sqlite)
could be downloaded from online version. 

Here is a 20-second-video to show briefly how it works:

https://user-images.githubusercontent.com/49595269/216095659-49ff5ed6-20e2-4a51-bf9d-e9bed337b5a9.mp4

### Modifications:

Here are the applied modifications to switch engine defined at [Tutorial 01](https://github.com/X-I-A/xia-tutorial-api-01). 

* models/purchase_order.py:
    * Importing a sqlite engine `from xia_engine_sql import SqliteEngine` (also need to add dependency in `requirements-xia.txt`)
    * Setting engine type as class attributes: `_engine = SqliteEngine`
    * Setting database location as class attributes: `_address = {"sqlite": {"_db": "db", "database": "./static/db.sqlite", "check_same_thread": False}}`
    * Giving key fields of data model: `_key_fields = ["po_number"]`

This is all what you need to do to change from an engine to another.


## Data engine types

There is no database which is capable to handle everything. 
Even some databases seem to be able to handle more workload types, they do the "extra" workload in an inefficient way.

So we need the coordination of different data engine to cover all needs. Here are the principal data engine types:

* Document data engine: Flexible data type with CRUD task
* Relational data engine: CRUD task and Transactional analytics
* Bigdata data engine: Large data stock and Large scale analytics
* Timeseries data engine: Realtime dashboard / alert
* Cache data engine: Low latency tasks
* Message data engine: Ingestion and dispatching data
* Rest data engine: Encapsulation of data engine as REST web service
* General data engine: Any stateful service could be used as data engine. 
For example, it is easy to encapsulate Github's API endpoint to simulate a data engine.

At last, you could use a composite engine to accomplish complex tasks by using multiple engines at the same time.


### Going deeper on data engine topic
[Tutorial 02-01](https://github.com/X-I-A/xia-tutorial-api-02-01): Analytical Query
[Tutorial 02-02](https://github.com/X-I-A/xia-tutorial-api-02-02): Data engine connection
[Tutorial 02-03](https://github.com/X-I-A/xia-tutorial-api-02-03): Batch input/output
[Tutorial 02-04](https://github.com/X-I-A/xia-tutorial-api-02-04): Data replication
[Tutorial 02-05](https://github.com/X-I-A/xia-tutorial-api-02-05): Composite Engine


### Next Step: Create first users for your data services

Data has value when it could help us to make a decision. Let's move to the next tutorial to discuss the user management

* [Tutorial 03](https://github.com/X-I-A/xia-tutorial-api-03): User Authentication
* [Tutorial 04](https://github.com/X-I-A/xia-tutorial-api-04): Authorization Management
* [Tutorial 05](https://github.com/X-I-A/xia-tutorial-api-05): Applying rate limits // Payment
* [Tutorial 06](https://github.com/X-I-A/xia-tutorial-api-06): Making independent microservice work as a complex application 
* [Tutorial 07](https://github.com/X-I-A/xia-tutorial-api-07): Examples of complex application
