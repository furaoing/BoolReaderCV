Launch Python API Server Command:
/opt/anaconda3/bin/python3.5 /apps/BoolReaderCV/PythonAPI/my_http.py &

Launch Docker Container Command:
sudo docker run -d --name boolreadercv -p 6680:6680 furaoing/boolreadercv:with_python_tf /bin/bash -c "/apps/opencv_server/opencv.out.1.0.2;/opt/anaconda3/bin/python3.5 /apps/BoolReaderCV/PythonAPI/my_http.py"
