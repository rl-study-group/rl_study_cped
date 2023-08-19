import torch
from accelerate import Accelerator

def prepare_model(model):
    accelerator = Accelerator()
    model = accelerator.prepare(model)
    return model

model = torch.nn.Linear(10, 2)

model = prepare_model(model)

inputs = torch.randn(4, 10)
outputs = model(inputs)
print(outputs.shape)


