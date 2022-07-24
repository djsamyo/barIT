# barIT


UV damage, fading from condensation and humidity, highlighter marks and discoloration are just some of the ways that barcodes can become unreadable to industrial barcode scanners. 
Damaged barcodes can lead to cargo loss, and global financial impact of such cargo loss exceeds $50Billion annually. We leverage existing cutting-edge AI technology to solve this real-world problem, addressing all the practical implications of the issue, and creating a solution that is ready for industrial implementation. 

Our software detects barcodes from images, classifies more than 5 types of barcode damage and reconstructs the correct barcodes in a user-friendly way that allows a warehouse worker to immediately replace potentially unreadable barcodes.
We use advanced deep learning classifiers and segmentation models, like the Xception UNet, integrated with a simplistic and user friendly interface. 

# Code

## Models
### Segmentation: 
Detects the barcode location and generates a binary image mask (0,1) using an RGB image of a barcode in any orientation in any setting. 
Uses an Xception Style U Net Image Segmentation Model

### Classification: 
Classifies the detected and correctly oriented barcode into one of two classes: damaged or not damaged
Uses a ResNet101v2 model pretrained on ImageNet weights then trained on artificially damaged barcodes

### Reconstruction: 
Takes in a damaged barcode image and generates a reconstructed readable image of the same barcode 
Uses a sequential model that encodes and then decodes the input image

## Data Processing

## Generating Correctly Oriented Data using Masks: 
Uses OpenCV to find the orientation angle of the barcode using the mask, rotates the original image by that angle, and then crops it to a horizontal rectangle

## Generate Damaged Data: 
Creates artificially damaged data using OpenCV by applying translucent boxes and color distortions, and then generating training datasets using modified images. 
