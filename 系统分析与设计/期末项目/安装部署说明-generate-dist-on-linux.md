from src code to dist
1. install git  
    $ sudo apt install git  
2. download the project source code  
    $ mkdir ~/github  
    $ cd ~/github  
    $ git clone https://github.com/ssad2019/web-client.git  
3. install nodejs and npm  
    $ mkdir ~/nodejs  
    $ cd ~/nodejs  
    $ wget https://nodejs.org/dist/v10.9.0/node-v10.9.0-linux-x64.tar.xz  
    $ tar xf  node-v10.9.0-linux-x64.tar.xz  
    $ sudo ln -s ~/nodejs/node-v10.9.0-linux-x64/bin/npm /usr/local/bin/  
    $ sudo ln -s ~/nodejs/node-v10.9.0-linux-x64/bin/node /usr/local/bin/  
  check node and npm version:  
    $ node --version  
      v10.9.0  
    $ npm --version  
      6.2.0  
  use taobao cnpm  
    $ npm install -g cnpm --registry=https://registry.npm.taobao.org  
    $ sudo ln -s ~/nodejs/node-v10.9.0-linux-x64/bin/cnpm /usr/local/bin/  
4. install dependency  
    $ cd ~/github/web-client  
    $ cnpm install  
5. test runnable  
    $ cd ~/github/web-client  
    $ cnpm run serve  
      waiting for compiling, this will probably takes you a few seconds  
    when it compile ok, open your browser and enter localhost:8080 into the address  
    if the web page display correctly ,then it runs ok  
6. build  
    $ cd ~/github/web-client  
    $ cnpm run build  
      waiting for a few seconds to build the project, you will see the build result under "~/github/web-client/dist"  
7. test if the dist can be deployed  
    $ cnpm install -g serve  
    $ sudo ln -s ~/nodejs/node-v10.9.0-linux-x64/bin/serve /usr/local/bin/  
    $ cd ~/github/web-client  
    $ serve -s dist  
      follow the output of the console, enter http://localhost:5000 into address bar of your browser  