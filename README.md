
## As the weights file is too large to upload pre-trained weights, you will need to train the network from scratch and the effect may be slower to improve, it is recommended to set the training epoch to a larger size.


## YOLOX-TBP：Implementation of this model in Pytorch
---

## Catalogue

1. [Specification of dependencies.]

2. [Training code.]

3. [Evaluation code.]

4. [table of results. ]



##### Specification of dependencies #####

Please see the requirements.txt.



##### Network training #####


Hyperparameters for training settings:   
   
                      fp16                = False
                      mosaic              = True
                      mosaic_prob         = 0.5
                      mixup               = True
                      mixup_prob          = 0.5
                      special_aug_ratio   = 0.7
                      UnFreeze_Epoch      = 400
                      Unfreeze_batch_size = 2
                      Init_lr             = 1e-2
                      Min_lr              = Init_lr * 0.01
                      optimizer_type      = "sgd"
                      momentum            = 0.937
                      weight_decay        = 5e-4

Add pre-training weights to the following section of train.py：

    model_path      = 'model_data/baseline-ep001-loss4.888-val_loss4.682.pth' 

If you do not have a pre-trained weights file, you do not need to add a path

Run [train.py] directly to start training.   



##### Prediction of training results ##### 


In the [yolo.py] , modify model_path and classes_path to correspond to the trained files in the following sections; model_path corresponds to the weights file under the logs folder, and classes_path is the class into which model_path corresponds:
           
       model_path      =  'model_data/ep215-loss3.735-val_loss3.773.pth'


      classes_path    =  'model_data/visdrone_classes.txt'


Run  [predict.py]  for single image inference, run it and enter the image path to detect it.



##### Access to assessment results #####：  

The evaluation results are available by running [get_map.py] and are saved in the map_out folder.



##### table of results #####

|       Training data set      |                  Pre-training weights               |         Test data set       |  image size | mAP 0.5 |


|    VisDrone2021-trainset     |       baseline-ep001-loss4.888-val_loss4.682.pth    |    VisDrone2021-testset-dev |  1600×1600  |   67.00  |




The experiment is conducted on Ubuntu 18.04.5 LTS, using an Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz and an NVIDIA Tesla A100 GPU. 
