# Nelson_Model_Dashboard
This Dashboard was created to display the Nelson Model results as graphs over a series of time. 

Running Nelson Model Dashboard with Docker

    With docker installed on your machine or server, running 'sh build.sh' will build the docker image
    running 'sh run.sh' will deploy the docker container

    The ports and ip can be changed in the last line of app.py where it says 'host=' and 'port=' and in the run.sh file (The default is http://0.0.0.0:8050)

Running Nelson Model Dashboard without Docker

    You must first install all the dependencies by running 'pip install -r requirements.txt'
    Then to start the web app run 'python3 app.py' 
