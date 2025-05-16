def test_with_image(image_path):
    frame = cv2.imread(image_path)
    if frame is None:
        print("Image not found or invalid.")
        return
    result_frame = detect_and_save(frame)
    cv2.imshow('Car Detection', result_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Then call:
test_with_image("car_image.jpg")
