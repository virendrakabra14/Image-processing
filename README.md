<h1>Image processing</h1>

<h3>1. Image compression: k-means clustering algorithm</h3>

Original Image (Size: 135 KB)<br><br>
<img src="./k-means/image.jpeg" style="width: 200px; height: auto;">

Compressed images with k values:<br>
<table>
  <tr>
    <th>k value</th>
    <th>Image</th>
    <th>Size (in KB)</th>
  </tr>
  <tr>
    <td>2</td>
    <td><img src="./k-means/k_2.jpeg" style="width: 200px; height: auto;"></td>
    <td>53</td>
  </tr>
  <tr>
    <td>3</td>
    <td><img src="./k-means/k_3.jpeg" style="width: 200px; height: auto;"></td>
    <td>57</td>
  </tr>
  <tr>
    <td>10</td>
    <td><img src="./k-means/k_10.jpeg" style="width: 200px; height: auto;"></td>
    <td>92</td>
  </tr>
  <tr>
    <td>64</td>
    <td><img src="./k-means/k_64.jpeg" style="width: 200px; height: auto;"></td>
    <td>96</td>
  </tr>
</table>

```
For Windows: python.exe kmeans.py
```

<h3>2. Noise reduction</h3>
Removal of salt-and-pepper noise using a median filter (window size: 3):<br><br>
<table>
  <tr>
    <th>Corrupted image</th>
    <th>Reconstruction</th>
  </tr>
  <tr>
    <td><img src="./median-filter/einstein.jpg" style="width: 200px; height: auto;"></td>
    <td><img src="./median-filter/einstein_better.jpg" style="width: 200px; height: auto;"></td>
  </tr>
  <tr>
    <td><img src="./median-filter/woman.jpg" style="width: 200px; height: auto;"></td>
    <td><img src="./median-filter/woman_better.jpg" style="width: 200px; height: auto;"></td>
  </tr>
  <tr>
    <td><img src="./median-filter/monalisa.png" style="width: 200px; height: auto;"></td>
    <td><img src="./median-filter/monalisa_better.png" style="width: 200px; height: auto;"></td>
  </tr>
</table>

```
For Windows: python.exe median-filter.py <image-path>
```
