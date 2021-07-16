

#### Importing custom modules in Google Collab

https://stackoverflow.com/questions/52733786/how-to-import-custom-modules-in-google-colab
  
import numpy as np
import math

from google.colab import drive
drive.mount('/content/drive')

import sys
sys.path.append('/content/drive/MyDrive/collab_custom_modules/utils')

#### /collab_custom_modules/utils folder has file utility.py with function printUtil

import utility as utl
utl.printUtil('Hi')

-----------------------------------------------


