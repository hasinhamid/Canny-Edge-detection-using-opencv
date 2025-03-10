import cv2
import glob
import os


output_dir = "C:\\Users\\junai\\IdeaProjects\\python\\dubotech\\output_edges"
os.makedirs(output_dir, exist_ok=True)
image_paths = glob.glob("C:\\Users\\junai\\IdeaProjects\\python\\dubotech\\main_img/*.jpg")
for img_p in image_paths:
    img=cv2.imread(img_p)
    img=cv2.resize(img,(400,400))
    cv2.imshow("before",img)   #shows before pic but dont save it
    cv2.waitKey(0)              #click any key to treverse to the next pic
    #coverting to gray scale
    img_gray= cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #gaussian blur for better ditection
    Gimg= cv2.GaussianBlur(img_gray,(3,3),0)
    #canny edge 
    edge= cv2.Canny(Gimg,70,100)
    cv2.imshow("after",edge)   #shows after pic but dont save it
    cv2.waitKey(0) 

    #saving the canny img
    filename = os.path.basename(img_p)  
    output_path = os.path.join(output_dir, f"canny_{filename}")
    cv2.imwrite(output_path, edge)
    print(f"Saved: {output_path}")



cv2.destroyAllWindows()
    