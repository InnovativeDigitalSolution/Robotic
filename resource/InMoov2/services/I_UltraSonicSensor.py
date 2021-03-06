# -- coding: utf-8 --
# ##############################################################################
#                 ultra Sonic Sensor FILE
# ##############################################################################


#parse config
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
trigLeftPin=ThisServicePartConfig.getint('MAIN', 'trigLeftPin')
echoLeftPin=ThisServicePartConfig.getint('MAIN', 'echoLeftPin')
ultraSonicLeftArduino=ThisServicePartConfig.get('MAIN', 'ultraSonicLeftArduino')
ultraSonicLeftActivated=ThisServicePartConfig.getboolean('MAIN', 'ultraSonicLeftActivated')

trigRightPin=ThisServicePartConfig.getint('MAIN', 'trigRightPin')
echoRightPin=ThisServicePartConfig.getint('MAIN', 'echoRightPin')
ultraSonicRightArduino=ThisServicePartConfig.get('MAIN', 'ultraSonicRightArduino')
ultraSonicRightActivated=ThisServicePartConfig.getboolean('MAIN', 'ultraSonicRightActivated')

if ultraSonicRightActivated:
  ultrasonicRight = Runtime.start("ultrasonicRight", "UltrasonicSensor")
  
  try:
    ultraSonicRightArduino=eval(ThisServicePartConfig.get('MAIN', 'ultraSonicRightArduino'))
    ultrasonicRight.attach(ultraSonicRightArduino, trigRightPin, echoRightPin)
    i01.ultrasonicSensor=ultrasonicRight
    i01.speakBlocking(i01.localize("STARTINGULTRASONIC"))
    # range can also be retreieved in a blocking call
    print "ultrasonicRight test is: ", i01.getUltrasonicRightDistance()
  except:
    errorSpokenFunc('BADRDUINOCHOOSEN','ultra Sonic Sensor Right')
    ultraSonicRightActivated=False
    pass

if ultraSonicLeftActivated:
  ultrasonicLeft = Runtime.start("ultrasonicLeft", "UltrasonicSensor")
  
  try:
    ultraSonicLeftArduino=eval(ThisServicePartConfig.get('MAIN', 'ultraSonicLeftArduino'))
    ultrasonicLeft.attach(ultraSonicLeftArduino, trigLeftPin, echoLeftPin)
    i01.ultrasonicSensor=ultrasonicLeft
    i01.speakBlocking(i01.localize("STARTINGULTRASONIC"))
    # range can also be retreieved in a blocking call
    print "ultrasonicLeft test is: ", i01.getUltrasonicLeftDistance()
  except:
    errorSpokenFunc('BADRDUINOCHOOSEN','ultra Sonic Sensor Left')
    ultraSonicLeftActivated=False
    pass  
