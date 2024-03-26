#! /usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

readonly WORKERS_CNT=4

function main()
{
  apt-get -y update
  apt-get install -y iproute2
  apt-get -y install wrk
  ip a
  if ! gunicorn -b 0.0.0.0:81 myapp:app ; then
    echo "Failed to run gunicorn..."
    return 1
  fi

}

main $@
