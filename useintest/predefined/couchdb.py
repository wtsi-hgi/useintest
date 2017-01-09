from useintest.services._builders import DockerisedServiceControllerTypeBuilder

_repository = "couchdb"
_ports = [5984]
_start_detector = lambda log_line: "Apache CouchDB has started" in log_line
_persistent_error_detector = lambda log_line: "no space left on device" in log_line

_common_setup = {
    "repository": _repository,
    "start_detector": _start_detector,
    "persistent_error_detector": _persistent_error_detector,
    "ports": _ports
}

CouchDB1_6DockerisedServiceController = DockerisedServiceControllerTypeBuilder(
    name="CouchDB1_6DockerisedServiceController",
    tag="1.6",
    **_common_setup).build()   # type: type

CouchDBLatestDockerisedServiceController = DockerisedServiceControllerTypeBuilder(
    name="CouchDBLatestDockerisedServiceController",
    tag="latest",
    **_common_setup).build()   # type: type


CouchDB1_6ServiceController = CouchDB1_6DockerisedServiceController
CouchDBServiceController = CouchDBLatestDockerisedServiceController

couchdb_service_controllers = {CouchDB1_6ServiceController, CouchDBServiceController}