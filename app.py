import streamlit as st
import transformers
from transformers import AutoProcessor, AutoModelForCausalLM
from PIL import Image, ImageDraw
import torch
import numpy as np
import random
import copy

# Define colormap for bounding boxes
colormap = ['blue','orange','green','purple','brown','pink','gray','olive','cyan','red',
            'lime','indigo','violet','aqua','magenta','coral','gold','tan','skyblue']

# Load Florence-2 model
st.title("Florence-2 Streamlit Deployment")
model_id = 'microsoft/Florence-2-large'

@st.cache_resource()
def load_model():
    model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True, device_map='cuda')
    processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
    return model, processor

model, processor = load_model()
st.success("Model Loaded Successfully")

def run_example(task_prompt, image):
    inputs = processor(text=task_prompt, images=image, return_tensors="pt")
    generated_ids = model.generate(
      input_ids=inputs["input_ids"].cuda(),
      pixel_values=inputs["pixel_values"].cuda(),
      max_new_tokens=1024,
      early_stopping=False,
      do_sample=False,
      num_beams=3,
    )
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
    parsed_answer = processor.post_process_generation(
        generated_text,
        task=task_prompt,
        image_size=(image.width, image.height)
    )
    return parsed_answer

def draw_ocr_bboxes(image, prediction):
    draw = ImageDraw.Draw(image)
    bboxes, labels = prediction['quad_boxes'], prediction['labels']
    for box, label in zip(bboxes, labels):
        color = random.choice(colormap)
        new_box = (np.array(box)).tolist()
        draw.polygon(new_box, width=3, outline=color)
        draw.text((new_box[0]+8, new_box[1]+2), label, fill=color)
    return image

# Streamlit UI
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    task = st.selectbox("Choose a Task", ["<CAPTION>", "<DETAILED_CAPTION>", "<OD>", "<OCR>", "<OCR_WITH_REGION>"])
    if st.button("Run Florence-2"):
        result = run_example(task, image)
        st.write("### Generated Output:")
        st.write(result)
        
        if task == "<OCR_WITH_REGION>":
            output_image = copy.deepcopy(image)
            output_image = draw_ocr_bboxes(output_image, result['<OCR_WITH_REGION>'])
            st.image(output_image, caption="OCR Bounding Boxes", use_column_width=True)
