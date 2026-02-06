import cv2
import mediapipe as mp

def main():
    # Initialize MediaPipe Face Detection
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils

    # For webcam input:
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    with mp_face_detection.FaceDetection(
        model_selection=0, min_detection_confidence=0.7) as face_detection:
        
        print("Press 'q' to quit.")
        
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_detection.process(image)

            # Draw the face detection annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            if results.detections:
                for detection in results.detections:
                    mp_drawing.draw_detection(image, detection)
                    
                    # Draw confidence score
                    score = detection.score[0]
                    bboxC = detection.location_data.relative_bounding_box
                    ih, iw, _ = image.shape
                    
                    # Calculate text position
                    x, y = int(bboxC.xmin * iw), int(bboxC.ymin * ih) - 10
                    
                    cv2.putText(image, f'{score:.2%}', (x, y), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                    
                    # Draw custom blue rectangle (BGR)
                    cv2.rectangle(image, (int(bboxC.xmin * iw), int(bboxC.ymin * ih)), 
                                  (int((bboxC.xmin + bboxC.width) * iw), int((bboxC.ymin + bboxC.height) * ih)), 
                                  (255, 0, 0), 2)

            # Flip the image horizontally for a selfie-view display.
            image = cv2.flip(image, 1)
            
            # Add instruction text
            cv2.putText(image, "Press 'q' to exit", (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
            
            cv2.imshow('MediaPipe Face Detection', image)
            
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
