# seinfeldSensor

This repository contains a python script that was built to run on a raspberry pi and use this IR sensor: https://www.amazon.com/gp/product/B012ZZ4LPM/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1

You'll need to setup your python environment with the pygame package

Dumb line for the purpose of creating a useless commit

### Other tips for getting off the ground and running
+ In triggerBass.py you'll need to define the path of the sound clips you want to play with an absolute path
  + I cut up 10 different clips and have the code picking from them randomly, if you want it different, you'll have to change that code yourself
+ Your audio files can go where ever (because you are defining them with an absolute path), but mine were in a top level directory named "audio"
