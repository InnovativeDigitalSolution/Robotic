# ##############################################################################
#            *** RIGHT ARM ***
# ##############################################################################

  
  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
i01.isRightArmActivated()=0
ThisSkeletonPart=RuningFolder+'config/skeleton_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

  i01.isRightArmActivated()=ThisSkeletonPartConfig.getboolean('MAIN', 'i01.isRightArmActivated()') 

except:
  errorSpokenFunc('ConfigParserProblem','rightarm.config')
  pass  
 
# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if i01.isRightArmActivated()==1 and (ScriptType=="RightSide" or ScriptType=="Full")  or ScriptType=="Virtual":
  i01.isRightArmActivated()=1
  if RightPortIsConnected:
    rightArm = Runtime.create("i01.rightArm", "InMoovArm")
    rightArm.startPeers()
    #pffff :) we need to manualy load now to get last position to avoid breaking parts
    rightArm.bicep.load()
    rightArm.shoulder.load()
    rightArm.rotate.load()
    rightArm.omoplate.load()
    rightArm.startPeers()
    #end pffff :)    
    rightArm.bicep.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'bicep'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'bicep'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'bicep'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'bicep')) 
    rightArm.shoulder.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'shoulder'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'shoulder'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'shoulder'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'shoulder')) 
    rightArm.rotate.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'rotate'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'rotate'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'rotate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'rotate')) 
    rightArm.omoplate.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'omoplate'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'omoplate'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'omoplate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'omoplate')) 
    
  
    rightArm.bicep.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'bicep'))
    rightArm.shoulder.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'shoulder'))
    rightArm.rotate.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'rotate'))
    rightArm.omoplate.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'omoplate'))

    rightArm.bicep.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'bicep'))
    rightArm.shoulder.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'shoulder'))
    rightArm.rotate.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'rotate'))
    rightArm.omoplate.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'omoplate'))

    i01.startRightArm(MyRightPort,BoardTypeMyRightPort)
    
    
    rightArm.bicep.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'bicep'))
    rightArm.shoulder.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'shoulder'))
    rightArm.rotate.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rotate'))
    rightArm.omoplate.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'omoplate'))
      
    rightArm.rest()
    
    rightArm.bicep.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'bicep'))
    rightArm.shoulder.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'shoulder'))
    rightArm.rotate.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'rotate'))
    rightArm.omoplate.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'omoplate'))

  else:
    #we force parameter if arduino is off
    i01.isRightArmActivated()=0