import cv2

# Создание объекта VideoCapture для захвата видеопотока
cap = cv2.VideoCapture(0)

# Чтение и отображение видеопотока
while True:
    ret, frame = cap.read()  # чтение кадра из видеопотока
    cv2.imshow('Webcam', frame)  # отображение кадра

    # Прерывание цикла при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Закрытие видеопотока и окна отображения
cap.release()
cv2.destroyAllWindows()