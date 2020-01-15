[![CircleCI](https://img.shields.io/circleci/project/github/iotwx/chords-mqtt-orchestrator/master.svg?style=for-the-badge&logo=circleci)](https://circleci.com/gh/iotwx/chords-mqtt-orchestrator/tree/master)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/iotwx/chords-mqtt-orchestrator/code-style?logo=github&style=for-the-badge)

# CHORDS MQTT Orchestrator

This package provides a tool to push MQTT messages to a [CHORDS portal]().

## Setup

### Clone this repository

```shell
git clone ...
```

### Modify `config.yaml`

You will need to modify the [chords_mqtt/config.yaml](chords_mqtt/config.yaml)
to your specifications.  ALL fields must be properly setup. Pay special attention that
your `topics` are correct.

If you run into trouble after installing when running, check your `~/chords_mqtt/config.yaml` and make
sure the correct information was included in that file.

An example config might look like this:

```yaml
mqtt:
  host: yourmq.tt
  port: 1883
  topics: ['iotwx']
chords:
  base_api_endpoint: 'http://yourchor.ds'
  api_key: '1234567890'
  email: 'yoda@jediacadem.ie'
```


### Run `setup.py` to install

```shell
python setup.py install
```

### Run the Orchestrator

To run the orchestrator, simply execute:

```
chords-orchestrator
```

Have fun!
