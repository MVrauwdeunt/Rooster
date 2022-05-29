#!/usr/local/bin/python
# coding: utf8

import yaml

def read_secrets():
    secrets_path = "config.yaml"
    with open(secrets_path, "r") as f:
        secrets = yaml.safe_load(f)
        return secrets