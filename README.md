# ROS Test Action


## Usage

Add a `test.yml`

```yml
name: Test

on:
  workflow_dispatch:
  pull_request:
  push:
    branches:
      - main

jobs:
  release:
    name: Test
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/greenroom-robotics/ros_builder:latest
      options: --user root

    steps:
      - name: Checkout this repository
        uses: actions/checkout@v3

      - name: Test
        uses: Greenroom-Robotics/ros_test_action@main
        with:
          token: ${{ secrets.API_TOKEN_GITHUB }}
```
