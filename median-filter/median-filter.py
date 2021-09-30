import numpy as np
from PIL import Image
import argparse
from os.path import splitext

parser = argparse.ArgumentParser (description = 'File to be read.')
parser.add_argument('file', help = 'Give the path to a file, on the command line. To be read.')
args = parser.parse_args()

img = Image.open(args.file).convert("L")
inArr = np.array(img)

# odd number: window size
n = 9
m = (n-1)//2

# use padding for border cases
inArr = np.pad (inArr, m, mode='edge')

rows = inArr.shape[0]
cols = inArr.shape[1]

outArr = np.copy(inArr)

grid = np.zeros((n,n))

for i in range(m, rows-m):
    for j in range(m, cols-m):
        grid = inArr[i-m:i+m,j-m:j+m]
        outArr[i][j] = np.median(grid)      # assign median value

img = Image.fromarray(outArr.astype(np.uint8))
img.save(splitext(args.file)[0]+'_better'+splitext(args.file)[1])   # save image