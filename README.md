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
  test:
    name: Test
    runs-on: ubuntu-latest

    steps:
      - name: Test
        uses: Greenroom-Robotics/ros_test_action@main
        with:
          token: ${{ secrets.API_TOKEN_GITHUB }}
```
