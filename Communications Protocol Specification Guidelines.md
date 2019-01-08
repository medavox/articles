Spec(ish)
====

Lists everything a new comms protocol must contain to be complete.

Think of it as a template for writing a spec, for your own custom protocol.

Also might make suggestions on formatting etc.


* list of byte structures (eg types composed of basic types) used throughout the protocol
    - valid ranges/values for basic types
* list of messages
    - with their exact byte structure
    - composed of byte structures (see above) and basic types
    - when this message can be sent
    - by whom
    - expected preceding messsage(s), expected following
* a flowchart which describes what order messages can occur in validly
