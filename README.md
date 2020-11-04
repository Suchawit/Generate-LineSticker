# Generate-LineSticker

## Preparing Dataset

Dataset contains ***4 folders*** and each one is divided into ***category, taste and character*** available to access [**line-sticker-data**](https://github.com/steerapi/line-sticker-data?fbclid=IwAR3cNJ9LHBSd9mmh-C8_Zsv7wfqgjswT3VyiGOzpNIDvCzvEfRCrVMEXjtc)<br>

**To install dataset**

     !pip install linestickerdata==0.0.12
**To see the list of available data** (Dict type)

     linestickerdata.list_available()
**To download and extact sticker**

     linestickerdata.get_image_paths(folder="Name_of_folder", character="Name_of_character", n=5, num_workers=1, seed=0)
     linestickerdata.get_image_paths(folder="Name_of_folder", category="Name_of_category", n=5, num_workers=1, seed=0)
     linestickerdata.get_image_paths(folder="Name_of_folder", taste="Name_of_taste", n=5, num_workers=1, seed=0)
where `n` is the number of stickers to download, and `num_workers` is the number of workers that use to download the stickers. [**Here is example**](https://github.com/Suchawit/Generate-LineSticker/blob/main/Preparedataset/Download%20all%20image.ipynb)

## Preprocessing Data

Use [**Model**](https://github.com/qhgz2013/anime-face-detector) to crop line sticker face

Also apply [**human face recognition model**](https://github.com/ageitgey/face_recognition) to seperate human face from sticker line face


## Training network using CycleGAN

