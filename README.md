🖼️ Florence-2 Streamlit Deployment
This is a Streamlit-based web application that leverages the power of Microsoft's Florence-2-large vision-language model to perform multiple multimodal tasks, including:

🖋️ Image Captioning

🧠 Detailed Captioning

🔍 Object Detection

🔡 Optical Character Recognition (OCR)

🗺️ OCR with Region-wise Bounding Boxes

🚀 Demo

(Insert GIF or image of app here)

🔧 Features
🧠 Powered by Microsoft Florence-2

⚡ Real-time image analysis using Streamlit

🎨 Bounding boxes over OCR regions

🖼️ Upload image & select task via UI

✅ Cached model loading for faster performance

📦 Requirements
Install dependencies via pip:

bash
Copy
Edit
pip install streamlit transformers torch torchvision pillow
🧠 Model Used
Model ID: microsoft/Florence-2-large

Library: 🤗 Hugging Face Transformers

Device: CUDA (GPU) support via device_map='cuda'

🏗️ How It Works
Upload an image via the Streamlit interface.

Select one of the multimodal tasks from the dropdown:

<CAPTION> – Basic image captioning

<DETAILED_CAPTION> – More descriptive captions

<OD> – Object detection

<OCR> – Text extraction from image

<OCR_WITH_REGION> – OCR with visual bounding boxes

Click Run Florence-2.

View generated output. If OCR with regions is selected, bounding boxes are overlaid on the image.

📂 File Structure
bash
Copy
Edit
📁 your-project/
│
├── app.py               # Main Streamlit app (code above)
├── README.md            # You're reading this!
🖼️ Example Output
Input Image:

(Insert sample image)

Task: <OCR_WITH_REGION>


🔒 Notes
Make sure your environment supports GPU (device_map='cuda') for smooth model execution.

Florence-2 models are large and may require significant VRAM.

📌 To Run the App
bash
Copy
Edit
streamlit run app.py
🤝 Contributing
Feel free to fork, improve, or create PRs! Bug reports and suggestions are welcome.

📃 License
MIT License. © 2025 [Your Name or GitHub Link]

Let me know if you'd like a logo, a hosted Hugging Face Spaces version, or instructions for deploying on Hugging Face / Streamlit Cloud!








