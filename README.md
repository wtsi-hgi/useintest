[![Build Status](https://travis-ci.org/wtsi-hgi/startfortest.svg)](https://travis-ci.org/wtsi-hgi/startfortest)
[![codecov.io](https://codecov.io/gh/wtsi-hgi/startfortest/graph/badge.svg)](https://codecov.io/github/wtsi-hgi/startfortest)
# Start For Test 
*I don't care how it's done, just start one of those so I can test my application with it!*

## Introduction
### Key Features
- Simple way of running services (e.g. Mongo, CouchDB, iRODS).
- No knowledge of containers required.
- No knowledge of service required (how to install it, when it's ready to use, etc.).
- Does not require the installation of anything on your local machine, aside from Docker.
- Makes it simple to test against multiple versions of the same service.
- Easy to achieve test isolation.

### Why use this library?
Software no longer works in isolation; with the trend towards microservices over monoliths, modern day applications 
rely on numerous external services for both data and computation.

Mocks can be a quick way to test against something that (should) behave like the external service that your 
application uses. However, unless a well respected mocking framework exists, the mock you'll end up with will probably 
make the same bad assumptions about the behaviour of service as your faulty code does!

Testing with the "real thing" or a shared dev mirror of it is probably not a good idea during development, 
particularly if the services that you're using hold state. You want to be able to run the tests in parallel, have 
repeatability and have availability, be it for when you're offline or for collaborators outside of your organisation. 
You also want to be able to wipe the slate clean and start again if something goes terribly wrong! It is unlikely you'll
be able to do this in any kind of shared environment.

This library offers a way to just start up services and then throw them away after each test case, with no mess left 
over on your machine. It gives complete test isolation along with confidence that you're testing with services similar 
to those used in production.


## How to use?
### Prerequisites
- Python >= 3.5.2
- Docker >= 1.12.3 (must be running)

### Installation
Bleeding edge versions can be installed directly from GitHub:
```bash
$pip3 install https://github.com/wtsi-hgi/startfortest@master#startfortest
```

### Use
#### Overview
```python
from startfortest.service.mongo import MongoController

# Starts a containerised version of Mongo
controller = MongoController()              
# Blocks until container running the service has started
service = controller.start_service()      
# Use service in test
run_my_test(my_application, service.host, service.port)
# Stops the container running the service
controller.stop_service(service)                                 
```


#### Available Services
##### Mongo
In the `startfortest.service.mongo` module:
- `MongoController`: Latest version of Mongo available.
- `Mongo3Controller`: Mongo version 3.

##### CouchDB:
In the `startfortest.service.couchdb` module:
- `CouchDBController`: Latest version of CouchDB available.
- `CouchDB1_6Controller`: CouchDB version 1.6.

##### iRODS
In the `startfortest.service.irods` module:
- `IrodsController`: Latest version of iRODS available.  
- `Irods4_1_10Controller`: iRODS version 4.1.10.
