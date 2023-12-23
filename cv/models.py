import mediapipe as mp

class ModelResult():
    def __init__(self, dataList):
        self.dataList = dataList
        self.name = dataList['name']
        self.pointsCoordinates = self.dataList['pointsCoordinates']
        self.objectArea = self.dataList['objectArea']
        self.numberOfObjects = self.dataList['numberOfObjects']
        self.text = self.dataList['text']

    def load_data(self, data):
        self.name = data['name']
        self.pointsCoordinates = data['pointsCoordinates']
        self.objectArea = data['objectArea']
        self.numberOfObjects = data['numberOfObjects']
        self.text = data['text']

    def get_data(self):
        return self.dataList
    
    def get_name(self):
        return self.name
    
    def get_points_coordinates(self):
        return self.pointsCoordinates
    
    def get_object_area(self):
        return self.objectArea
    
    def get_number_of_objects(self):
        return self.numberOfObjects
    
    def get_text(self):
        return self.text

class FullBody():
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_holistic = mp.solutions.holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.dictResult = self.get_clear_data()
        self.modelResult = ModelResult(self.get_clear_data())
        
    
    def get_clear_data(self):
        return {
                        'name': 'fullbody',
                        'pointsCoordinates': [],
                        'objectArea': 0,
                        'numberOfObjects': 0,
                        'text': ''
                        }

    def process(self, frame):
        result = self.mp_holistic.process(frame)
        self.save_landmark_data(result)
        

    def save_landmark_data(self, result):
        if result.pose_landmarks:
            landmarks = result.pose_landmarks.landmark
            for i, landmark in enumerate(landmarks):
                self.dictResult[i] = {'x': landmark.x, 'y': landmark.y, 'z': landmark.z}

            self.modelResult.load_data(self.dictResult)

    def get_data(self):
        return self.dictResult