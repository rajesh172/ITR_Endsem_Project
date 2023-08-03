import cv2
path = 'C:\Users\Patel\Pictures\black_dot.png'

# reading the image in grayscale mode
gray = cv2.imread(path, 0)

# threshold
th, threshed = cv2.threshold(gray, 100, 255,
		cv2.THRESH_BINARY|cv2.THRESH_OTSU)

# findcontours
cnts = cv2.findContours(threshed, cv2.RETR_LIST,
					cv2.CHAIN_APPROX_SIMPLE)[-2]

# filter by area
s1 = 3
s2 = 20
xcnts = []

for cnt in cnts:
	if s1<cv2.contourArea(cnt) <s2:
		xcnts.append(cnt)

# printing output
print("\nDots number: {}".format(len(xcnts)))
