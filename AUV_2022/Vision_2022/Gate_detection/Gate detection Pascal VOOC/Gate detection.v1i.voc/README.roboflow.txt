
Gate detection - v1 2022-04-10 5:01pm
==============================

This dataset was exported via roboflow.com on August 7, 2022 at 9:01 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 276 images.
Gate are annotated in Pascal VOC format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* Random rotation of between -7 and +7 degrees

The following transformations were applied to the bounding boxes of each image:
* 50% probability of horizontal flip
* Random shear of between -5° to +5° horizontally and -5° to +5° vertically


