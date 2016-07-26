# py-flamework-api

Base class for flamework-api derived API classes

## Usage - simple

### execute_method

```
from flamework.api.client import OAuth2

api = OAuth2(ACCESS_TOKEN, hostname=HOSTNAME, endpoint=ENDPOINT)

method = 'api.test.echo'

args = {
	'hello': 'world'
}

rsp = api.execute_method(method, args)
print rsp
```

## Usage - fancy

### execute_method_paginated

This is really just syntactic sugar to handle paginating all the results for a query in a single method call. It's just like calling `execute_method` except that you also define a callback to be invoked for every API call response.

```
from flamework.api.client import OAuth2

api = OAuth2(ACCESS_TOKEN, hostname=HOSTNAME, endpoint=ENDPOINT)

def cb(rsp):

	# do something with rsp here...
	# return True to signal that pagination should continue

	return True

method = "whosonfirst.places.search"
args = { "placetype": "venue", "iso": "gb", "extras": "geom:latitude,geom:longitude,sg:postcode", "per_page": 500 }

api.execute_method_paginated(method, args, cb)
```

## Contributors

* [Who's On First](https://github.com/whosonfirst)

## See also

* https://github.com/cooperhewitt/flamework-api
* https://github.com/cooperhewitt/flamework
