import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="1"
from scipy.spatial.distance import cosine
from keras.models import load_model
from utils import *
from FaceLiveness.RealTime import liveness
import cv2
import time
def recognize(img,
              encoder,
              items,
              boxes,
              recognition_t=0.30,
              confidence_t=0.99,
              required_size=(160, 160), ):
    #img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #results = detector.detect_faces(img_rgb)
    #results = detector.detectMultiScale(img_rgb)
    results = boxes
    for res in results:
        #if res['confidence'] < confidence_t:
            #continue
        #face, pt_1, pt_2 = get_face(img_rgb, res) #Hacer que realtime.py regrese esto
        face, pt_1, pt_2 = res
        encode = get_encode(encoder, face, required_size)
        encode = l2_normalizer.transform(encode.reshape(1, -1))[0]
        name = 'Desconocido'

        distance = float("inf")
        for db_name, db_encode in items:
            dist = cosine(db_encode, encode)
            if dist < recognition_t and dist < distance:
                name = db_name
                distance = dist

        if name == 'Desconocido':
            cv2.rectangle(img, pt_1, pt_2, (0, 0, 255), 2)
            cv2.putText(img, name, pt_1, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
        else:
            cv2.rectangle(img, pt_1, pt_2, (0, 255, 0), 2)
            cv2.putText(img, name + f'__{distance:.2f}', (pt_1[0], pt_1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 200, 200), 2)
    return img


if __name__ == '__main__':
    encoder_model = r'/home/misaelzazueta/PycharmProjects/Facenet-Liveness/FaceNet/model/facenet_keras.h5'
    encodings_path = r'/home/misaelzazueta/PycharmProjects/Facenet-Liveness/FaceNet/encodings/encodings.pkl'
    #face_detector = mtcnn.MTCNN()
    #face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    face_encoder = load_model(encoder_model)
    encoding_dict = load_pickle(encodings_path)
    items = encoding_dict.items()

    vc = cv2.VideoCapture(r'/home/misaelzazueta/PycharmProjects/Facenet-Liveness/test.mp4')
    #vc = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=640, height=480, format=(string)NV12, framerate=(fraction)20/1 ! nvvidconv flip-method=rotate-180 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink' , cv2.CAP_GSTREAMER)
    while True:
        ret, frame = vc.read()
        if not ret:
            print("no frame:(")
            break
        frame = cv2.rotate(frame, cv2.cv2.ROTATE_90_CLOCKWISE)
        st = time.time()
        boxes = liveness(frame)
        if boxes:
            frame = recognize(frame, face_encoder, items, boxes)
        cv2.imshow('Camera', frame)
        print("Total")
        print(time.time()-st)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            break
    vc.release()
    cv2.destroyAllWindows()
