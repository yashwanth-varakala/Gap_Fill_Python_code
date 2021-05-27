import c3d
import gapfill as gf
import numpy as np

reader = c3d.Reader(open('P02_FL_Con_2FP_noGapFill.c3d', 'rb'))

for i, points, analog in reader.read_frames():
   print('frame {}: point {}, analog {}'.format(i, points.shape, analog.shape))


n=9463

gap_fill=gf.fill_marker_gap_interp() 
