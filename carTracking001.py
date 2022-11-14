import cv2

jpg_filename = 'cars-test.jpg'
video_filename = 'cars002.mp4'
xml_filename = 'cars.xml'

img = cv2.imread(jpg_filename)
bnw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

video1 = cv2.VideoCapture(video_filename)
car_tracker = cv2.CascadeClassifier(xml_filename)



while True:
    (read_successful, frame1) = video1.read()

    if read_successful:
        framegs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    else:
        break

    recognized_cars = car_tracker.detectMultiScale(framegs)
    print( recognized_cars ) # ok -> this is working!


    for ( top1, left1, width1, height1) in recognized_cars:
        cv2.rectangle( frame1, ( top1, left1), ( top1 + width1, left1 + height1), (0, 255, 0) , 2)

    cv2.imshow('TEST002', frame1)
    k = cv2.waitKey(20)

    if k == 113:
        break


video1.release()



# ====================================================================================================

# for picutre
#recognized_cars = car_tracker.detectMultiScale(bnw)
#print( recognized_cars ) # ok -> this is working!


# ( top1, left1, width1, height1) just this kind of assign recognized_cars[0] 
# ( top1, left1, width1, height1) = some_car 

# for ( top1, left1, width1, height1) in recognized_cars:
#   cv2.rectangle( img, ( top1, left1), ( top1 + width1, left1 + height1), (0, 255, 0) , 2)

# ====================================================================================================


#cv2.imshow('TEST001', img)
#cv2.waitKey()

# ====================================================================================================




print('Done')