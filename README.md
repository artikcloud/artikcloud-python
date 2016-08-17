ARTIK Cloud Python SDK
================
[![PyPI version](https://badge.fury.io/py/artikcloud.svg)](https://badge.fury.io/py/artikcloud)

This SDK helps you connect your Python scripts to ARTIK Cloud. The SDK helps authenticating with ARTIK Cloud, and exposes a number of methods to easily execute REST API calls to ARTIK Cloud.

## Requirements.
Python 2.7 and later.

## Setuptools
You can install the bindings via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install
```

Or you can install from Github via pip:

```sh
pip install git+https://github.com/artikcloud/artikcloud-python.git
```

To use the bindings, import the package:

```python
import artikcloud
```

## Manual Installation
If you do not wish to use setuptools, you can download the latest release.
Then, to use the bindings, import the package:

```python
import path.to.artikcloud
```

## Getting Started

Peek into [tests](https://github.com/artikcloud/artikcloud-python/tree/master/tests) for examples about how to use the Python SDK.

In addtion, you can look at our tutorial and sample applications. These will give you a good overview of what you can do and how to do it.

## Tests

(Please make sure you have [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) installed)

 Execute the following command to run the tests in the current Python (v2 or v3) environment:

```sh
$ make test
[... magically installs dependencies and runs tests on your virtualenv]
Finished processing dependencies for artikcloud==2.0.0
test_send_message (tests.test_messages_api.MessagesApiTests) ... ok
test_get_user_devices (tests.test_users_api.UsersApiTests) ... ok
test_get_self_async (tests.test_users_api.UsersApiTests) ... ok
test_get_self (tests.test_users_api.UsersApiTests) ... ok
...
Ran 4 tests in 13.905s

OK
```
or

```
$ mvn integration-test -rf :ArtikCloudClientTests
...
Finished processing dependencies for artikcloud==2.0.0
test_send_message (tests.test_messages_api.MessagesApiTests) ... ok
test_get_self (tests.test_users_api.UsersApiTests) ... ok
test_get_self_async (tests.test_users_api.UsersApiTests) ... ok
test_get_user_devices (tests.test_users_api.UsersApiTests) ... ok
...
Ran 4 tests in 14.330s

OK
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 31.999 s
[INFO] Finished at: 2016-04-06T14:26:48-07:00
[INFO] Final Memory: 12M/309M
[INFO] ------------------------------------------------------------------------
```
If you want to run the tests in all the python platforms:

```sh
$ make test-all
[... tox creates a virtualenv for every platform and runs tests inside of each]
  py27: commands succeeded
  py34: commands succeeded
  congratulations :)
```

More about ARTIK Cloud
-------------------------

If you are not familiar with ARTIK Cloud, we have extensive documentation at https://developer.artik.cloud/documentation

The full ARTIK Cloud API specification can be found at https://developer.artik.cloud/documentation/api-reference/

Check out advanced sample applications at https://developer.artik.cloud/documentation/samples/

To create and manage your services and devices on ARTIK Cloud, create an account at https://developer.artik.cloud

Also see the ARTIK Cloud blog for tutorials, updates, and more: http://artik.io/blog

License and Copyright
---------------------

Licensed under the Apache License. See [LICENSE](https://github.com/artikcloud/artikcloud-python/blob/master/LICENSE).

Copyright (c) 2016 Samsung Electronics Co., Ltd.
