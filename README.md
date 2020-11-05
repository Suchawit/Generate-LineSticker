# Generate-LineSticker
<img src="https://github.com/Suchawit/Generate-LineSticker/blob/main/Img/Sample_sticker.PNG" width="1000px"/>

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
### Other Datasets
To change the style and feature of other images to Line sticker style applied these two datasets: 

Face dataset can be downloaded from [**Here**](https://www.kaggle.com/ciplab/real-and-fake-face-detection)

<img src="https://github.com/Suchawit/Generate-LineSticker/blob/main/Img/Sample_human_face.PNG" width="400px"/>

Sketch dataset can downloaded from [**Here**](http://www.cs.cmu.edu/~mengtial/proj/sketch/)

<img src="https://github.com/Suchawit/Generate-LineSticker/blob/main/Img/Sample_sketch.PNG" width="400px"/>

## Training Network without Preprocessing Data
CycleGAN is implemented using torch for collection style transfer ppurpose required unparied two datasets for more detail please access [**Here**](https://github.com/junyanz/CycleGAN). After install and create requirement virsual ennvironment for CycleGAN. Divided Line sticker into two folders, first folder is called trainA and second is called testA which trainA and testA contains 1610 images and 500 images from

      get_image_paths(folder=data['folder'], character= row['taste'], n=5, num_workers=1, seed=0)
      get_image_paths(folder=dataofficial['folder'], character= row['taste'], n=5, num_workers=1, seed=0)
      get_image_paths(folder=dataofficial-th['folder'], character= row['taste'], n=5, num_workers=1, seed=0)
      get_image_paths(folder=data-th['folder'], character= row['taste'], n=5, num_workers=1, seed=0)
      
Then seperate face dataset into trainB and testB as well as sketch dataset

      python train.py --dataroot ./sticker2face --name maps_sticker2face --model cycle_gan
      python train.py --dataroot ./sticker2sketch --name maps_sticker2sketch --model cycle_gan

`./sticker2face` directory is where the Line sticker and face datasets are. `./sticker2sketch` directory is where the Line sticker and sketch datasets are 
### Results
Sticker to face trained for 200 epochs<br />                               Sticker to sketch trained for 66 epochs

<img src="https://github.com/Suchawit/Generate-LineSticker/blob/main/Img/Results_sticker2face.PNG" width="300px"/>


## Preprocessing Data

Since the results from training network without preprocessing data tend to overfit by trying to generate unknown letters or characters, Apply [**anime face detector**](https://github.com/qhgz2013/anime-face-detector) and [**face recognition**](https://github.com/ageitgey/face_recognition) to crop Line sticker face and seperate human face which will be used to train with humman face dataset specifically. See illustration below

## Training network using with Preprocessing Data

