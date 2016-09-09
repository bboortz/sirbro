#!/bin/bash
set -i

URL="<UNSET>"
if [ -z "$BASE_URL" ]; then
	BASE_URL="http://localhost:8080/api"
fi

set_url() {
	local version="$1"

	if [ -z "$version"  -o "$version" == "" ]; then
		URL="${BASE_URL}"
	else
		URL="${BASE_URL}/${version}"
	fi
}

get_api_call() {
	local param="$1"

	curl --fail --insecure -H "Content-Type: application/json" -X GET "${URL}/${param}"
	echo
	curl --fail --insecure -H "Content-Type: text/plain" -X GET "${URL}/${param}"
	echo
	curl --fail --insecure -X GET "${URL}/${param}"
	echo
}


###

set_url "v1"
get_api_call "alive"
get_api_call "info"
get_api_call "config"

set_url 
get_api_call "alive"
get_api_call "info"
get_api_call "config"

