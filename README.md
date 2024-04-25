# Viam Machine Creation and Provisioning

Once you have your project at a stage where you are ready to provision many machines, going through the user interface will likely become too cumbersome. Viam therefore provides you easy to use API as part of our SDKs to manage organizations, locations and machines.
This is a simply Python example which allows you to input a name and the number of machines you want to create and will output one machine-id.json file per machine created. This json file contains the same information as your would get it from the app.viam.com / viam.json and can be used to setup and connect your actual machine.

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

