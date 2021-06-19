# Stupid-FishEye-undistortion-Batch-with-a-GUI

#### 1. start the backen sever `python server.py`

#### 2. Open the web browser like Chrome, safari, and so on. The address is: `http://127.0.0.1:5000/index.html`

#### 3. Copy your images into the folder:  `html/example/data`

#### 4. To find a suitable parameter, you can drag any picture of your data to the web. If you can not see the correction parameter, you can adapt the size of the web browser.

#### 5. Adjust the parameter until  you fell it is OK. You can also drag another picture from the foloder to the web browser to see if the colibration is also fit to other figures. 

#### 6. When you fell the parameter meet your requirenment:

- Right mouse click and chose the `inspection element `
- Chose the `console`
- Input:  `startRunning();`
- Then the web will show the calibrated results one by one. And it will give you a alert if all pictures are processed.

#### 7. Check the results in `export`


(I didnt wrote the instrution but I mean I don't want to spend any time on correct things above anyway so good luck folks)


The project is based on https://github.com/jywarren/fisheyegl

