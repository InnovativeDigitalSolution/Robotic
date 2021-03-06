# ##############################################################################
#            *** HEAD ***
# ##############################################################################


  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
isHeadActivated=0

#read current skeleton part config
ThisSkeletonPart=RuningFolder+'config/skeleton_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

  isHeadActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isHeadActivated') 
  MouthControlActivated=ThisSkeletonPartConfig.getboolean('MOUTHCONTROL', 'MouthControlActivated')
  AudioSignalProcessing=ThisSkeletonPartConfig.getboolean('AUDIOSIGNALPROCESSING', 'AudioSignalProcessing')
  AnalogPinFromSoundCard=ThisSkeletonPartConfig.getint('AUDIOSIGNALPROCESSING', 'AnalogPin')
  if ScriptType=="Virtual":AnalogPinFromSoundCard=3
  HowManyPollsBySecond=ThisSkeletonPartConfig.getint('AUDIOSIGNALPROCESSING', 'HowManyPollsBySecond')
  MouthControlJawMin=ThisSkeletonPartConfig.getint('MOUTHCONTROL', 'MouthControlJawMin')
  MouthControlJawMax=ThisSkeletonPartConfig.getint('MOUTHCONTROL', 'MouthControlJawMax')
  MouthControlJawTweak=ThisSkeletonPartConfig.getboolean('MOUTHCONTROL', 'MouthControlJawTweak')
  MouthControlJawdelaytime=ThisSkeletonPartConfig.getint('MOUTHCONTROL', 'MouthControlJawdelaytime')
  MouthControlJawdelaytimestop=ThisSkeletonPartConfig.getint('MOUTHCONTROL', 'MouthControlJawdelaytimestop')
  MouthControlJawdelaytimeletter=ThisSkeletonPartConfig.getint('MOUTHCONTROL', 'MouthControlJawdelaytimeletter')
  jawMIN=ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'jaw')
  jawMAX=ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'jaw')
  neckRest=ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'neck')
  rotheadRest=ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rothead')
  neckPin=ThisSkeletonPartConfig.getint('SERVO_PIN', 'neck')
except:
  isHeadActivated=0
  errorSpokenFunc('CONFIGPARSERPROBLEM','head.config')
  pass

isRollNeckActivated=ThisSkeletonPartConfig.getboolean('ROLLNECKSERVO', 'isRollNeckActivated') 
RollNeckArduino=ThisSkeletonPartConfig.get('ROLLNECKSERVO', 'RollNeckArduino')

# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isHeadActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full") or ScriptType=="Virtual":
  isHeadActivated=1
  if LeftPortIsConnected:
    head = Runtime.create("i01.head","InMoov2Head")
    head.startPeers()
    #pffff :) FIXME? we need to manualy load now to get last position to avoid breaking parts 
    #head.neck.load()
    #head.rothead.load()
    #head.rollNeck.load()
    #end pffff :)
    #map    
    head.jaw.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'jaw'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'jaw')) 
    head.eyeX.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'eyeX'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'eyeX'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'eyeX'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'eyeX')) 
    head.eyeY.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'eyeY'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'eyeY'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'eyeY'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'eyeY')) 
    head.neck.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'neck'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'neck'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'neck'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'neck')) 
    head.rothead.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'rothead'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'rothead'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'rothead'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'rothead'))
    head.rollNeck.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'rollneck'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'rollneck'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'rollneck'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'rollneck'))
  
    #maxspeed
    #head.neck.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'neck'))
    #head.rothead.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'rothead'))
    #head.rollNeck.setMaxSpeed(ThisSkeletonPartConfig.getint('MAX_SPEED', 'rollneck'))
     
    head.jaw.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'jaw'))
    head.eyeX.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'eyeX'))
    head.eyeY.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'eyeY'))
    head.neck.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'neck'))
    head.rothead.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rothead'))
    head.rollNeck.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rollneck'))

    head.jaw.setPin(ThisSkeletonPartConfig.getint('SERVO_PIN', 'jaw'))
    head.eyeX.setPin(ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyeX'))
    head.eyeY.setPin(ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyeY'))
    head.neck.setPin(ThisSkeletonPartConfig.getint('SERVO_PIN', 'neck'))
    head.rothead.setPin(ThisSkeletonPartConfig.getint('SERVO_PIN', 'rothead'))
    head.rollNeck.setPin(ThisSkeletonPartConfig.getint('SERVO_PIN', 'rollneck'))
  
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'jaw'):head.jaw.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'eyeX'):head.eyeX.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'eyeY'):head.eyeY.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'neck'):head.neck.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'rothead'):head.rothead.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'rollneck'):head.rollNeck.setInverted(True)

    #i01.startHead(MyLeftPort,BoardTypeMyLeftPort,ThisSkeletonPartConfig.getint('SERVO_PIN', 'neck'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'rothead'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyeX'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyeY'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'rollneck'))
    i01.startHead(MyLeftPort)
    rollneck=head.rollNeck
    
    #overide rollneck arduino
    try:
      RollNeckArduino=eval(RollNeckArduino)
    except:
      errorSpokenFunc('BADRDUINOCHOOSEN',', Roll Neck')
      isRollNeckActivated=0
      pass  
    
    if isRollNeckActivated:
      head.rollNeck.detach(left)
      head.rollNeck.attach(RollNeckArduino,ThisSkeletonPartConfig.getint('SERVO_PIN', 'rollNeck'),ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rollNeck'),ThisSkeletonPartConfig.getint('MAX_SPEED', 'rollNeck'))
     
    rotheadEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'rothead')
    neckEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'neck')
    rollneckEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'rollneck')
    eyeXEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'eyeX')
    eyeYEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'eyeY')
    
    #head.jaw.setMaxSpeed(500)

    head.rest()
    
    head.rothead.setAutoDisable(rotheadEnableAutoDisable)
    head.neck.setAutoDisable(neckEnableAutoDisable)
    head.rollNeck.setAutoDisable(rollneckEnableAutoDisable)
    head.jaw.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'jaw'))
    head.eyeX.setAutoDisable(eyeXEnableAutoDisable)
    head.eyeY.setAutoDisable(eyeYEnableAutoDisable)
    
# ##############################################################################
#                 Software mouth control
# ##############################################################################    
    
    if MouthControlActivated and AudioSignalProcessing==False:
      i01_mouthControl = Runtime.createAndStart("i01.mouthControl","MouthControl")
      #i01.startMouthControl(i01_head.jaw,i01_mouth)
      i01_mouthControl.setmouth(MouthControlJawMin,MouthControlJawMax)
      print "software mouthcontrol activation"
      if MouthControlJawTweak:i01_mouthControl.setDelays(MouthControlJawdelaytime, MouthControlJawdelaytimestop, MouthControlJawdelaytimeletter)
# ##############################################################################
#                 mouth control based on audio signal processing
# ##############################################################################  
    
    #please set aref
    if AudioSignalProcessing:
      i01.setMute(False)
      left.addListener("publishPinArray","python","publishMouthcontrolPinLeft")
      AudioSignalProcessing=False
      MouthControlActivated=False
      AudioSignalProcessingCalibration=1
      left.enablePin(AnalogPinFromSoundCard,HowManyPollsBySecond)
      i01.speakBlocking(i01.localize("MOUTHSYNCRONISATION"))
      
      
      AudioSignalProcessingCalibration=0
      maxAudioValue=maxAverage(AudioInputValues,10)
      AudioInputValues=[]
      AudioSignalProcessingCalibration=1
      sleep(3)
      AudioSignalProcessingCalibration=0
      minAudioValue = (sum(AudioInputValues) / len(AudioInputValues)) + 20
      left.disablePin(AnalogPinFromSoundCard)
      result=0
      #arduino dit not detect analog value
      if minAudioValue>50:
        i01.speakBlocking(i01.localize("MOUTHSYNCRONISATION")+str(AnalogPinFromSoundCard))
        result=1
      #arduino detect a poor value
      if result==0 and (maxAudioValue-minAudioValue<=255):
        head.jaw.map(minAudioValue,maxAudioValue,jawMIN,jawMAX)
        AudioSignalProcessing=True
        i01.speakBlocking(i01.localize("MOUTHSYNCRONISATIONNOTPERFECT"))
      #arduino detect a good value  
      if result==0 and (maxAudioValue-minAudioValue>255):
        head.jaw.map(minAudioValue,maxAudioValue,jawMIN,jawMAX)
        AudioSignalProcessing=True
        i01.speakBlocking(i01.localize("MOUTHSYNCRONISATIONOK"))
        
      print maxAudioValue,minAudioValue
      
   
  else:
    #we force parameter if arduino is off
    isHeadActivated=0
    MouthControlActivated=0
    
else:
  MouthControlActivated=0
