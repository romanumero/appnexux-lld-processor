## AppNexus Log Level Query Engine

### Introduction
The application allows AppNexus users to make sense of their audiences utilizing log level data (LLD). This applications efficiently imports large amounts of raw log data, applies processing logic to simplify querying, and provides tools for non-technical users to build specific audiences, create campaign monitors, reports, and custom rules.


### Data Models

AppNexus LLD is supports protobuf (version 2.5.0) delimited, protobuf, and TSV. This implementation supports protobuf-delimited format and limited to the AppNexus Standard Feed. These data files have around 120 columns, about half of which are relevant.

#### `users` Data Model

The columns of interested are:

|Field             |Mapping      |
|:-----            |:-----       |
|user_id_64        | direct map of int value -> row ID       |
|device_unique_id| adnxs_device_unique_id(device_unique_id):int -> row ID|
|country         | direct map of country code -> row ID        |
|region | direct map of region code -> row ID|
|dma | adnxs_dma(dma):int -> row ID|
|city | adnxs_city(city):int -> row ID|
|postal_code| adnxs_postal_code(postal_code):int -> row ID|
|operating_system| adnxs_os(operating_system_id):int -> row ID|
|browser| adnxs_browser(browser_id):int -> row ID|
|language| adnxs_language(language_id):int ->  row ID|
|site_domain| direct map of string value -> row ID|
|device_type| adnxs_device_type(device_type) -> row ID|
|device_id| adnxs_device_id(device_id):int -> row ID|
|carrier_id|adnxs_carrier_id(carrier_id):int -> row ID|
|gender| direct map of enum int -> row ID|
|age | direct map of age int -> row ID|









Requires:
- Python 3.4+
- Pilosa 1.2.0+

Setup:
- Pull the official image - `docker pull pilosa/pilosa:latest`
- Make sure it's installed successfully - `docker run -p 10101:10101 --rm pilosa/pilosa:latest`