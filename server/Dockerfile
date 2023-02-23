# 可以到https://hub.docker.com/r/paddlepaddle/serving/tags选择适合部署环境的镜像，这里选择cpu环境的基础镜像。
FROM paddlepaddle/serving:0.7.0-devel 

# 安装程序运行的依赖
RUN python3.7 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple \
	paddle-serving-client==0.7.0 \
	paddle-serving-app==0.7.0 \
	faiss-cpu==1.7.1post2 \
	paddle-serving-server==0.7.0 \
	paddlepaddle==2.2.0 

WORKDIR /server
COPY . /server
WORKDIR /server/paddleserving/recognition
CMD python3.7 recognition_web_service.py
