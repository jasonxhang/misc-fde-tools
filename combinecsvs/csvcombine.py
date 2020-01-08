import os
import glob
import pandas as pd
os.chdir("/combinecsvs")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]