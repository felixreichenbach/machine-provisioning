# Viam Machine Creation and Provisioning

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install viam-sdk
```

## Configuration

Create a `.env` file and set the appropriate values:

``` 
API_KEY_ID=<YOUR VALUE>
API_KEY=<YOUR VALUE>
LOCATION_ID=<YOUR VALUE>
```

## Execute and fill in the prompts

- Machine name prefix
- Number of machines

```
python3 client.py
```

