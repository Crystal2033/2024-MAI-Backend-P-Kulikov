#! /usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

readonly WORKERS_CNT=4

function main()
{
  #-----------THIS IS FOR WRK ANALYSIS
  apt-get -y update
  apt-get install -y iproute2
  apt-get -y install wrk
  ip a
  #-----------THIS IS FOR WRK ANALYSIS-----------
  if ! gunicorn --workers ${WORKERS_CNT} -b 0.0.0.0:81 myapp:app ; then
    echo "Failed to run gunicorn..."
    return 1
  fi

}

main $@
