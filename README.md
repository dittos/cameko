```
curl -O http://www.udp.jp/software/nvxs-1.0.2.tar.gz
tar xzvf nvxs-1.0.2.tar.gz
cd nvxs-1.0.2
./configure
make
sudo make install
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
pip install git+https://github.com/dittos/python-animeface --allow-external PIL --allow-unverified PIL
```
