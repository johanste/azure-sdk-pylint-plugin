# azure-sdk-pylint-plugin

Investigating how to create pylint plugins/checkers to automate compliance checks for some of the Azure Library for Python design guidelines.
The current state of the project is highly experimental. Please don't use any code in this repository as an example on how to write good plugins.

Some ideas on rules:

* Check for approved method name prefixes (list, get, create etc.)
* Check API signatures based on prefixes (parameters, including **kwargs/documentation)
* Check return type/noun used in method name (e.g. list_things should return Thing:s, not Stuff:s)
* Check class name prefixes
* Check class name suffixes (use client as suffix - e.g. FooClient)
* Check canonical pattern (create_configuration, configuration class etc.)
* Verify that paged implementations follow our protocol
* Verify that we don't use positional parameters in our code when we have multiple arguments
* Ensure that we are sync or async "all the way through" for REST calls.
* Ensure that public APIs log the right things
* Ensure that exceptions explicitly raised are documented
* Ensure that exceptions derive from one of the approved exception types
* Ensure that we have type annotations
