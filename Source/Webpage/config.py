# THRESHOLD
CFG_THRESHOLD = 0.5

# YOLO
CFG_PATH_YOLO_MODEL = './model/YOLOv5.pt'

# FASTER RCNN
CFG_PATH_FASTERRCNN_CONFIG = './model/config_FasterRCNN.txt'
CFG_PATH_FASTERRCNN_MODEL = './model/FasterRCNN.pth'

# DEVICE
CFG_DEVICE = 'cpu' # ['cpu' , 'cuda'] # FASTER RCNN

# MODEL
CFG_MODEL = 'darknet' # ['darknet' , 'yolo', 'fasterrcnn']

# HTTP SERVER
CFG_HTTP_TYPE = 'local' # ['local' , 'ngrok']

# CUSTOM
CFG_ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
CFG_PATH_UPLOAD = './static/uploads'
CFG_PATH_RESULT = './static/results'
CFG_MAX_CONTENT_LENGTH = 1024 * 1024 * 1024 * 1024 * 1024 # 5MB
