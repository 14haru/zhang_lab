# How to Install Multiple versions of tensor-flow-GPU, CUDA and cuDNN on the Windows

## You need to install the following containts before 1st step
- anaconda
- Microsoft Visual Studio
    - Tensor-flow-gpu requires a Nsight included in Visual studio.
- GPU Driver
    - Clean install is better way if already installed.

## 1. Check the versions
Check the versions that you want to install at this URL.\
https://www.tensorflow.org/install/source_windows#gpu


## 2. Install CUDA
### 2.1 How to install CUDA
You can install CUDA at this URL.\
https://developer.nvidia.com/cuda-toolkit-archive

If the installation is successful, You can see the path at "Edit the system environment variable" like this image.\
(If your Windows language is Japanese, It is called "システム環境変数の編集".)

```
CUDA_PATH_V10_0 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0
CUDA_PATH_V11_2 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2
```

![path_image](./images/system_environment_variable.PNG)

### 2.2 How to install multiple versions of the CUDA on one environment
You can install multiple versions of CUDA by installing in the same way as 2.1.\
If you install two different versions of CUDA, CUDAs are installed as shown in the following image.

![CUDA_file](./images/CUDA_file.PNG)

## 3. Install cuDNN
## **Note the supported CUDA version**
The same version of cuDNN may support different versions of CUDA.

You can install cuDNN at this URL.(You need to log in to your NVIDIA account.)\
https://developer.nvidia.com/rdp/cudnn-archive

1. Unzip the file
2. Copy and paste the unzipped file's bin, include and lib into the folder where CUDA is installed and overwrite it.

Example of CUDA installed path
```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2
```
![paste_here](./images/paste_here.PNG)



## References
https://qiita.com/momendoufu/items/6a0bc0701d797ef5b727
https://hahaeatora.hateblo.jp/entry/2020/06/30/200000


## 4 Restart the PC
Restart the PC to set the path.

