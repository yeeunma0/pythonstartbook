import torch

print(torch.__version__)
print(torch.backends.mps.is_built())
print(torch.backends.mps.is_available())