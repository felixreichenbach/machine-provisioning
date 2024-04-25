"""A simple sample script useful to learn about creating machines in app.viam.vom"""
import asyncio
import os
from viam.rpc.dial import DialOptions
from viam.app.viam_client import ViamClient
from dotenv import load_dotenv

load_dotenv()

async def connect():
    """Connect to app.viam.com"""
    # Set API_KEY and API_KEY_ID in the .env file with the appropriate values
    # .env example:
    # API_KEY_ID=XXXXX
    # API_KEY=XXXXX
    # LOCATION_ID=XXXXX
    #
    dial_options = DialOptions.with_api_key(os.getenv("API_KEY"), os.getenv("API_KEY_ID"))
    return await ViamClient.create_from_dial_options(dial_options)


async def main():
    """Main"""
     # Make a Viam app client
    viam_client = await connect()
    # Instantiate a ProvisioningClient to run provisioning client API methods on
    app_client = viam_client.app_client

    # Delete all robots in the location
    # robots = await app_client.list_robots(os.getenv("LOCATION_ID"))
    # for robot in robots:
    #     await app_client.delete_robot(robot.id)
    #     print("Robot deleted: " + robot.id)
    
    # Prompt user for information to create new machines
    name = input("Enter the machine name prefix:")
    number = int(input("Enter the number of machines to create:"))
    # Create machines based upon user input
    robot_ids = []
    for i in range(number):
        robot_ids.append(await app_client.new_robot(name+"_"+str(i),os.getenv("LOCATION_ID")))
    # 
    for i in robot_ids:
        robot_parts = await app_client.get_robot_parts(i)
        if (len(robot_parts) > 1):
            raise ValueError("Robot has more than one part, this is not supported")
        f = open(i+".json", "w", encoding="utf-8")
        f.write("{\"cloud\":{\"app_address\":\"https://app.viam.com:443\",\"id\":\""+robot_parts[0].id+"\",\"secret\":\""+robot_parts[0].secret+"\"}}")
        f.close()

    # Don't forget to close the machine when you're done!
    viam_client.close()


if __name__ == "__main__":
    asyncio.run(main())
