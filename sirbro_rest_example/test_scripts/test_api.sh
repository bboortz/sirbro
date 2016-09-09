#!/bin/bash
set -i

VERSION="v1"

if [ -z "$URL" ]; then
	URL="http://localhost:8080/api/${VERSION}"
fi

get_api_call() {
	local param="$1"

	curl --fail --insecure -H "Content-Type: application/json" -X GET "${URL}/${param}"
	echo
	curl --fail --insecure -H "Content-Type: text/plain" -X GET "${URL}/${param}"
	echo
	curl --fail --insecure -X GET "${URL}/${param}"
	echo
}

get_api_call "alive"
get_api_call "info"
get_api_call "config"

