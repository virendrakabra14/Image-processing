# The k-means algorithm partitions n observations into k clusters
# with each observation belonging to the cluster with the nearest mean (centroid),
# the centroid serving as a prototype of the cluster

# Iteration-based

# Choose k points in the dataset (these are the initial 'centroids').
# Calculate distance of each point from each centroid.
# Assign points closest to a centroid to that cluster.
# At the end, re-compute the centroids.
# Repeat until new and old centroids are almost same (i.e., within a given error bound).

import cv2
import numpy as np
import matplotlib.pyplot as plt

def myKmeans (data, k, max_iter, error):
    
    centroidList = data[:k] # first k rows

    for i in range(max_iter):

        labels = np.empty((data.shape[0],1), dtype=int)     # each pixel has a 'label', that is the index of the cluster that 
                                                            # this pixel belongs to
        total = 0

        prevCentroidList = np.copy(centroidList)    # centroids of the previous iteration (for computing error)
        sums = np.zeros((k,3))
        nums = np.zeros((k,3))

        for j in range(data.shape[0]):

            norms = np.empty((k,1))

            for m in range(k):
                norms[m] = np.linalg.norm (data[j] - centroidList[m])   # norm is the 3-dimensional Euclidean norm

            labels[j] = np.argmin(norms, axis=0)

            sums[labels[j]] = sums[labels[j]] + data[j]
            nums[labels[j]] = nums[labels[j]] + np.ones((1,3))
        
        near = True

        for k1 in range(k):
            centroidList[k1] = sums[k1]/nums[k1]
            if (np.linalg.norm(centroidList[k1]-prevCentroidList[k1]) > error):     # check with previous values
                near = False
        
        if (near == True or i == max_iter-1):
            return (labels, centroidList)

        
#########################


image = cv2.imread("image.jpeg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# reshape the image to a 2D array of pixels and 3 color values (RGB)
pixels = image.reshape((-1, 3))
# convert to float
pixels = np.float32(pixels)

# number of clusters (k)
k = 3
labels, centers = myKmeans(pixels, k, 10, 1.0)
# pixels = data (numpy array (2D) of pixel values)
# k = no. of clusters
# 10 (3rd arg) = max. no. of allowed iterations
# 1 (4th arg) = error threshold (i.e., the max. distance that a cluster centroid may 'move' in consecutive iterations, for successful end of algorithm)

# 'labels, centers' names and argument order has been kept in sync with the cv2 library's kmeans function
# 'centers' is the array of coordinates of cluster centroids
# 'labels' are the respective cluster numbers that points belong to

# 8 bit values
centers = np.uint8(centers)

# make 'labels' 1D
labels = labels.flatten()

# convert all pixels to the color of the centers
newImage = centers[labels.flatten()]

# reshape back to the original image dimension
newImage = newImage.reshape(image.shape)

# show the image
plt.imshow(newImage)
plt.savefig('k_'+str(k)+'.jpeg')    # save the image
plt.show()