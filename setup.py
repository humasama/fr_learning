# Environment Setup in MacOS

1. Install conda and pyicu in a virtual environment
```
python3 -m venv myenv
source myenv/bin/activate
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh
source ~/miniconda3/bin/activate

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes

conda install -c conda-forge pyicu
```

2. Install polyglot
```
// https://mirrors.aliyun.com/pypi/simple
// https://pypi.douban.com/simple
pip install polyglot -i https://pypi.tuna.tsinghua.edu.cn/simple -v
which polyglot
```

3. install other dependency
```
pip install pycld2 morfessor six -i https://pypi.tuna.tsinghua.edu.cn/simple -v
```
