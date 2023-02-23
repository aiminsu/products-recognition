import os
import io
import json
import base64
import requests
from PIL import Image
import gradio as gr

def pil_to_base64(img_pil):
    imgByteArr = io.BytesIO()
    img_pil.save(imgByteArr, format='JPEG')
    img_bytes = imgByteArr.getvalue()
    pic_content = base64.b64encode(img_bytes).decode("utf-8")
    return pic_content

def search(image_base64):
    '''
    图片搜索
    '''
    url = "http://localhost:18081/recognition/prediction"
    data = {"key": ["image"], "value": [image_base64]}
    r = requests.post(url=url, data=json.dumps(data))
    return r.json()

# 提取特征并搜索
def inference(img_pil):
    pic_content = pil_to_base64(img_pil)
    response = search(pic_content)
    print("response:", response)
    value = response["value"][0].replace("'", '"')
    search_list = json.loads(value)
    output = []
    for item in search_list:
        img_path = os.path.join("gallery", item["rec_docs"].split("\t")[0])
        img = Image.open(img_path)
        label = item["rec_docs"].split("\t")[1]
        score = round(item["rec_scores"], 2)
        text = f"标签:{label} 分数:{score}"
        output.append((img, text))
    return output


# 配置gradio组件值
title = "饮料识别"
description = "上传Query图片，在Gallery图像库(约1k张)中进行搜索识别，默认返回相似分大于0.5的最相似结果。"

if __name__ == "__main__":
    # 开启服务
    interface = gr.Interface(
        fn=inference,
        inputs=[
            gr.inputs.Image(type="pil", label="Query"),
        ],
        outputs=[
            gr.Gallery(label="搜索结果", show_label=True, elem_id="gallery"
            ).style(grid=[3], height="auto"),
        ],
        examples=[["query/001.jpeg"], ["query/002.jpeg"], ["query/003.jpeg"], ["query/004.jpeg"], ["query/005.jpeg"]],
        title=title,
        description=description,
        allow_flagging='never',
        ).launch(server_name="0.0.0.0", server_port=7860, debug=False)