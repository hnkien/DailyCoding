import torch

# Tạo một tensor 3D
tensor_3d = torch.randn(2, 3, 4)

# Hoán đổi chiều 0 và chiều 2
transposed_tensor = tensor_3d.transpose(0, 2)

print("Kích thước trước khi hoán vị:", tensor_3d.shape)
print(tensor_3d)
print("Kích thước sau khi hoán vị:", transposed_tensor.shape)
print(transposed_tensor)
