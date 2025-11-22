# Image Filtering App (OpenCV + Streamlit)

Simple Streamlit app to apply several image filters (grayscale, brightness, stylization, vintage vignette, HDR/detail enhance) using OpenCV.

## Files
- `app.py` — main Streamlit application (upload image, choose filter, adjust sliders).
- `README.md` — this file.

## Requirements
- Python 3.8+
- Windows (tested)
- Python packages:
  - streamlit
  - opencv-contrib-python
  - pillow
  - numpy
  - matplotlib (optional)

Install recommended (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install streamlit opencv-contrib-python pillow numpy matplotlib
```
Or:
```powershell
pip install -r requirements.txt
```

## Run
From project root (c:\projects\cv):
```powershell
streamlit run app.py
```
Streamlit will print a local URL to open the app.

## Usage
1. Open the Streamlit app in your browser.
2. Upload an image (jpg, jpeg, png).
3. Select a filter from the dropdown and adjust available sliders.
4. The UI shows the Original and Filtered images side-by-side.

## Filters & Parameters
- None: no change.
- Black and White: converts to grayscale.
- Brightness: `level` slider (-50..50) — adjusts image brightness.
- Style: `sigma_s` (0..200), `sigma_r` (0.0..1.0) — OpenCV stylization parameters.
- Vintage: `level` (controls vignette strength).
- HDR: `level` (brightness) + `sigma_s`, `sigma_r` — uses detailEnhance.

## Notes & Troubleshooting
- Stylization and detailEnhance require `opencv-contrib-python` (not plain `opencv-python`).
- Images are loaded with PIL (RGB) and converted to NumPy arrays; Streamlit expects RGB for colored images and `channels='GRAY'` for grayscale.
- If functions raise errors, ensure image dtype is uint8: `img = img.astype('uint8')`.
- Adjust slider ranges in `app.py` as needed.
