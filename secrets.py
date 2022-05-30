#!/usr/local/bin/python
# coding: utf8

import yaml
import os


def read_secrets():
    secrets_path = os.path.dirname(os.path.abspath(__file__)) + "/config.yaml"
    with open(secrets_path, "r") as f:
        secrets = yaml.safe_load(f)
        return secrets

