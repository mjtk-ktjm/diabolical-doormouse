#!/bin/bash
docker-compose build
docker-compose run --rm --name build-staging-dev-env staged_dev  
