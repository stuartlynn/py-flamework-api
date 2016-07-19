# py-flamework-api

Base class for flamework-api derived API classes

## Example

	from flamework.api.client import OAuth2

	api = OAuth2(ACCESS_TOKEN, hostname=HOSTNAME, endpoint=ENDPOINT)

	method = 'api.test.echo'

	args = {
		'hello': 'world'
	}

	rsp = api.execute_method(method, args)
	print rsp

## Contributors

* [Who's On First](https://github.com/whosonfirst)

## See also

* https://github.com/cooperhewitt/flamework-api
* https://github.com/cooperhewitt/flamework
