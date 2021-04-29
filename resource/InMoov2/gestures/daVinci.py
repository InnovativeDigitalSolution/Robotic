def daVinci():
  i01.startedGesture()
  # get the current value of auto disable
  leftPreviousAutoDisableValue = i01.leftArm.omoplate.isAutoDisable()
  rightPreviousAutoDisableValue = i01.rightArm.omoplate.isAutoDisable()
  # turn off auto disable for this gesture
  i01.leftArm.omoplate.setAutoDisable(False)
  i01.rightArm.omoplate.setAutoDisable(False)
  i01.setHandSpeed("left", 100.0, 100.0, 100.0, 100.0, 100.0, 22.0)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 22.0)
  i01.setArmSpeed("left", 36, 36, 36, 36)
  i01.setArmSpeed("right", 36, 36, 36, 36)
  i01.setHeadSpeed(31.0, 31.0)
  i01.moveHead(80,90)
  i01.moveArm("left",0,118,29,74)
  i01.moveArm("right",0,118,29,74)
  i01.moveHand("left",50,40,30,20,10,47)
  i01.moveHand("right",50,40,30,20,10,137)
  sleep(5)
  # restore the auto disable value after the gesture is done.
  i01.leftArm.omoplate.setAutoDisable(leftPreviousAutoDisableValue)
  i01.rightArm.omoplate.setAutoDisable(rightPreviousAutoDisableValue)
  i01.finishedGesture()

