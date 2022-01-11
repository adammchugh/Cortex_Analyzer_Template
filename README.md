## Cortex Analyzer Template
[![Docker Image CI](https://github.com/adammchugh/Cortex_Analyzer_Template/actions/workflows/docker-image.yml/badge.svg?branch=development)](https://github.com/adammchugh/Cortex_Analyzer_Template/actions/workflows/docker-image.yml)
[![CodeQL](https://github.com/adammchugh/Cortex_Analyzer_Template/actions/workflows/codeql-analysis.yml/badge.svg?branch=development)](https://github.com/adammchugh/Cortex_Analyzer_Template/actions/workflows/codeql-analysis.yml)

### Usage

```console
$ pip install --user cortexutils==2.1.0

$ cat tests/input/input.json | jq
{
  "config": {
    "check_pap": true,
    "check_tlp": true,
    "delay": 10,
    "max_pap": 2,
    "max_tlp": 2
  },
  "data": "8.8.8.8",
  "dataType": "ip",
  "pap": 1,
  "tlp:": 1
}

$ python template.py tests

$ cat tests/output/output.json | jq
{
  "success": true,
  "summary": {
    "taxonomies": [
      {
        "level": "info",
        "namespace": "template",
        "predicate": "ip",
        "value": "8.8.8.8"
      }
    ]
  },
  "artifacts": [
    {
      "tags": [
        "template"
      ],
      "tlp": 2,
      "dataType": "ip",
      "data": "8.8.8.8"
    }
  ],
  "full": {
    "data": "8.8.8.8",
    "input": {
      "config": {
        "check_pap": true,
        "check_tlp": true,
        "delay": 0,
        "max_pap": 2,
        "max_tlp": 2
      },
      "data": "8.8.8.8",
      "dataType": "ip",
      "pap": 1,
      "tlp:": 1
    }
  }
}
```
aa