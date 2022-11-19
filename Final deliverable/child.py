	import time
	import wiotp.sdk.application
	print("Hello")
	myConfig={
		"identity":{
			"orgId":"af8k8g",
			"typeId":"Tracker",
			"deviceId":"12345",
		},
		"auth":{
			"token":"12345678"
		}
	}
	
	client=wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
	client.connect()
	while True:
		name="Child"
		latitude=17.4219272
		longitude=78.5488783
		myData={'name':name,'lat':latitude,'lon':longitude}
		client.publishEvent(eventId="status",msgFormat="json",data=myData,qos=0,onPublish=None)
		print("Data published to IBM IoT Platform: ",myData)
		time.sleep(5)
	client.disconnect()


