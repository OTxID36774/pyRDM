# pyRDM
WIP Module for RDM API Calls and Some extra Non API related interactions (Single/Multi Device Assignment swaps, etc)
Additionally playing with some raw Proto Handling for debugging and investigating useful info for RDM integration

## What this IS and what it ISN'T?
The pyRDM module is designed to provide a python base RDM class and appropriate methods for easy developement around RDMs current features. I'll do my best to keep everything up to date for all API requests from APIRequestHandler.swift.

**This is NOT, Intended to be a full scale application of any sort, I use this as an base RDM object for a flask setup I personally have, so the formatting and output of the API calls are designed around that application. If there is a desire for me to incorporate the subprocesses calls I used with ios-deploy/etc, I will at very least at an example/how to of what I do. Or if someone else would like to contribute, I can integrate a call of sorts like that here if need be**


the *requests* package is the only external requirement for pyRDM. All other requirements in the requirements.txt are related to the WIP Proto endpoints.

# Current Support as of 01/24/2019
**Initiate pyRDM object**
``` rdm = RDM(url,usr,pwd) ```
> Where url = http://rdmip:9000, usr = RDM Username, pwd = RDM password

## Available API Calls
- > Get Device Status = returns device status as List=[] of Dicts={key:value,...}
  - ```devices = rdm.show_devices()```
- > Get instance Status = returns instance status as List=[] of Dicts={key:value,...}
  - ```instances = rdm.show_instances()```
- > Get Assignments Status = returns Auto-Assignments as List=[] of Dicts={key:value,...}
  - ```assignments = rdm.show_assignments()```
- > Get Instance IV Queue = returns current Queue information as List=[] of Dicts={key:value,...}
  - ``` Queue = RDM.show_ivqueue(instance as str, formatted as str([boolean])) ```
**_Formatted defaults to false, and should be used this way, unless you intend to use a flask template with static image locations that mirror RDM's_**

## Available Non API RDM Controls
**_These calls work by capturing the CSRF and Session Token on Auth with RDM, and then use these to post to particular web endpoints_**
- > Before using anything of these calls you must set the header with the following method
  - ```rdm.setHeaders()```
- > Change device assignment = pass device name/uuid and instance name as strings
  - ```rdm.assignDevice(device, instance) ```
- > Change Multiple Devices Assignments = Pass a list assignments=[] of Dict() in format { 'device': "deviceName/uuid" , 'instance': "InstanceName" }
  - ```rdm.assignDevices(assignments) ```
  
## To Do for pyRDM calls:
1) I'll add the subprocess calls to run ios-deploy to remotely remove UIC Test Runner, Since I imagine that's why people asked to see this XD
- Additional support for RDM Controls
  - Remove device from RDM Backend
  - Clear Quests
  - Add or Remove Auto-Assignments (For those who desire multiple sets of autoassignments for particular days/events/etc)
  - Integrate modified version of [Racinel200's](https://github.com/racinel200) TSP solution ```RDM.TSP(instance, type, minlvl, maxlvl)```
    - The solution will allow you to select existing Instance and type, and perform TSP solution on the route. Prompt provides the ability to automatically add the new instance to RDM with minlvl and maxlvl settings if provided on call
