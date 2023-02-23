## 商品识别服务
基于pp-ShituV2搭建的商品识别服务可视化demo。服务端基于paddleserving运行，客户端基于gradio搭建。

![demo](demo.png)

### 服务端部署
```
cd server
# 构建镜像
docker build -t server:v1.0 .
# 启动服务
docker run -d -p 18081:18081 server:v1.0
```


### 客户端部署
```
cd client
# 启动服务
python app.py
```
浏览器输入部署机器IP:7860打开可视化界面。