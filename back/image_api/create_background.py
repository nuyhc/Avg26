import torch
from diffusers import StableDiffusionPipeline


from PIL import Image

color_dict = {
    "Joy":"yellow",
    "Panic/Anxiety":"white",
    "Anger":"orange",
    "Sadness/Hurt":"blue",
    "Neutral":"purple"
}
# 모델 경로
# 모델 위치 변경시, 경로 수정
model_path = r"C:/Users/anoth\Desktop/2023capstone/back/model_emotion_estimate.pt"

# Model Load
model_emotion = torch.hub.load("WongKinYiu/yolov7", "custom", model_path, force_reload=True)
background_generator = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
background_generator = background_generator.to("cuda")

# Create Background
# input_img: 관객 이미지 파일로 저장
# mood: 공연이 의도한 분위기/color dict keys와 동일하게
def create_background2(input_img: str, mood: str)->Image:
    print("create_background에 들어감")
    results = model_emotion(input_img).pandas().xyxy[0]
    label = results.groupby("name")[["class", "confidence"]].mean().reset_index(drop=False).sort_values("confidence").iloc[-1, 0]
    conf = results.groupby("name")[["class", "confidence"]].mean().reset_index(drop=False).sort_values("confidence").iloc[-1, -1]
    
    # if results.empty: prompt = f"A background with 50% {color_dict[mood]}"
    # else: prompt = f"A background with {conf*100:.2f}% {color_dict[label]}"
    if results.empty: prompt = f"art style background of feeling the emotion of {mood} with 50% {color_dict[mood]}"
    else: prompt = f"art style background of feeling the emotion of {label} with {conf*100:.2f}% {color_dict[label]}"
    
    
    background = background_generator(prompt).images[0]
    
    print('create_background 끝남')
    print(background)
    print(type(background))
    background.save('reuslt.png')
    return background