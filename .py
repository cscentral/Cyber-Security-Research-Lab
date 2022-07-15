import os

import time

import random

filename = "virus.py"

while True:

if os.path.exists(filename):

with open(filename, "w") as f:

f.write("#!/usr/bin/env python\n")

f.write("import os\n")

f.write("import time\n")

f.write("import random\n")

f.write("filename = \"virus.py\"\n")

f.write("while True:\n")

f.write("\tif os.path.exists(filename):\n")

f.write("\t\twith open(filename, \"w\") as f:\n")

f.write("\t\t\tf.write(\"#!/usr/bin/env python\\n\")\n")

f.write("\t\t\tf.write(\"import os\\n\")\n")

f.write("\t\t\tf.write(\"import time\\n\")\n")
