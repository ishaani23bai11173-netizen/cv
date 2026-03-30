import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

cv2.putText(img, "By Ishaani", (20,50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 0)

edges = cv2.Canny(blur, 100, 200)

cv2.putText(edges, "Edge Detection Output", (20,80),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

cv2.imshow("Ishaani Original Image", img)
cv2.imshow("Ishaani Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
