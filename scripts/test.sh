#!/bin/bash

./download_URLS_files.sh \
  --sources \
    '["git@github.com:HurleyKane/project_template.git",\
      "git@github.com:HurleyKane/crust.git",\
       "https://gitlab.com/libeigen/eigen/-/archive/5.0.0/eigen-5.0.0.zip"]' \
  --dest "./"