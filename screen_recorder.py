import cv2
import numpy as np 
import pyautogui

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('data//output.avi', fourcc, 20.0, (1366,768))
while(True):
    img = pyautogui.screenshot()
    frame = np.array(img,dtype=np.uint8)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    rec = np.ones((10,10),dtype=np.uint8)
    cv2.imshow("r" ,rec )
    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cv2.destroyAllWindows()