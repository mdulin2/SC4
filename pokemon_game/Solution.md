## Pokete Games - Level 1
- The code for getting the configuration file is
```
# The name for the given ENV
name = os.environ['USERNAME']
if(os.path.exists("/tmp/{}/pokete.json".format(name))):
	with open("/tmp/{}/pokete.json".format(name)) as _file:
		_si = json.load(_file)
```
- This takes in the environment variable ``USERNAME`` and combines this to create a path inside of ``/tmp/$USERNAME/pokete.json``. 
- flag: ``pokete.json``. 

## Pokete Games - Infinite Money 
- The file pokete.json contains all of the stored state of the game. From money, to map loading and many other things. 
- Edit the file ``/tmp/$USERNAME/pokete.json``. The variable is user specific. 
	- Can be edited via vim, nano or whatever else. 
- Edit the value of the JSON object ``money`` to be larger than 100000000. 
- Load the game and the flag should output.
- Flag: SC4{M0reM0neyM0Pr0b1ems-M13haelSc0Tt}

## Pokete Games - Cheating with Shinies
- The file pokete.json contains all of the stored state of the game. From money, to map loading and many other things. 
- Edit the file ``/tmp/$USERNAME/pokete.json``. The variable is user specific. 
	- Can be edited via vim, nano or whatever else. 
- Edit the first pokemon of the 'pokes' field to have the name ``pikachu``. 
- Edit the field ``shiny`` on the poke to be TRUE instead of FALSE.
- Load the game and the flag should output.
- Flag: SC4{ShinyShinyShinyShiny}

## Pokete Games - Teleportation
- The file pokete.json contains all of the stored state of the game. From money, to map loading and many other things. 
- Edit the file ``/tmp/$USERNAME/pokete.json``. The variable is user specific. 
	- Can be edited via vim, nano or whatever else. 
- The stage we need to get to has the name ``Arena of Agrawos``. 
	- If we search for this name, it only appears in the file ``maps.py``.
	- The key for each element is ``playmap_##``. In our case, this is playmap_46. 
- The field ``map`` indicates the current user map. Set this to be ``playmap_46``. 
- Load the game and the flag should output. 
- Flag: SC4{FlyPidgeyFly!}

## Pokete Games - Unintended Solution 
- The following code is part of the configuration loading process within pokete.py 
```
elif os.path.exists(HOME + "/.cache/pokete/pokete.py"):
	l_dict = {}
	with open(HOME + "/.cache/pokete/pokete.py", "r") as _file:
		exec(_file.read(), {"session_info": _si}, l_dict)
	_si = json.loads(json.dumps(l_dict["session_info"]))
```
- This is reading a file from a user controlled location and calls ``exec`` on it. 
	- The exec function executes raw native Python code!
- By creating this file with Python code, we can inject our own code in the process. 
- The code above only runs if the configuration file is not there. So, we need to delete it.
- Run the following bash commands to create the file with a shell in it: ``rm /tmp/$USERNAME/pokete.json; mkdir /tmp/$USERNAME/.cache; mkdir /tmp/$USERNAME/.cache/pokete; echo 'import os; os.system("/bin/bash")' > /tmp/$USERNAME/.cache/pokete/pokete.py``
- Flag: SC4{CodeXXXXXXXecutionDidntSeeThatOneComing!?}
