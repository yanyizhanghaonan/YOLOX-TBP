import torchvision.models as models
import torch
from nets.yolo_denset import YoloBody
from ptflops import get_model_complexity_info

with torch.cuda.device(0):
  model = YoloBody(10, 'l')
  flops, params = get_model_complexity_info(model, (3, 1600, 1600), as_strings=True, print_per_layer_stat=True) #不用写batch_size大小，默认batch_size=1
  print('Flops:  ' + flops)
  print('Params: ' + params)
