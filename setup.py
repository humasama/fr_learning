# Environment Setup in MacOS

1. Install polyglot in a virtual environment
```
python3 -m venv myenv
source myenv/bin/activate
// https://mirrors.aliyun.com/pypi/simple
// https://pypi.douban.com/simple
pip install polyglot -i https://pypi.tuna.tsinghua.edu.cn/simple -v
which polyglot
```

2. install dependency pyicu
```
// 1) install icu4c
ls /usr/local/Cellar/icu4c@77 //77.1
export ICU_VERSION=77
export PYICU_INCLUDES=/usr/local/Cellar/icu4c@77/77.1/include 
export PYICU_LFLAGS=-L/usr/local/Cellar/icu4c@77/77.1/lib 

// 2) install pyicu
pip install pyicu -i https://pypi.tuna.tsinghua.edu.cn/simple -v --upgrade
```

3. install other dependency
```
pip install pycld2 morfessor six -i https://pypi.tuna.tsinghua.edu.cn/simple -v
```
