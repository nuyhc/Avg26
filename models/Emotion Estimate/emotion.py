import torch
import cv2
import numpy as np
import pandas as pd

def emotion_extract(thr: int=0.5)->pd.DataFrame:
    model = torch.hub.load("ultralytics/yolov5", "custom", path=r"./ee_model.pt", force_reload=True)
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        result = model(frame)
        cv2.imshow("Detection", np.squeeze(result.render()))
        labels = result.pandas().xyxy[0]
        print(labels)
        if cv2.waitKey(10)&0xFF==ord("q"): break
    cap.release()
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    emotion_extract()