# VoterCRM - BackEnd
This is the backend part of the VoterCRM project.

## Technologies Used
- **Flask (v2.3.2)**: A lightweight web framework used for building the backend.
- **Python (v3.11.0**: The programming language used for developing the backend logic.
- **SQLAlchemy (v2.0.13)**: An ORM (Object-Relational Mapping) library used for interacting with the database.
- **MYSQL (v5.7 image)**: The chosen relational database management system.
- **PyJWT (JSON Web Tokens) (v2.7.0)**: A secure method for authentication and authorization.
- **Git (v2.39.1.windows.1)** : Version control system for tracking changes and collaboration.

## How to build locally

1. git clone https://github.com/SanBud/VoterCRM_Backend.git

2. cd VoterCRM_Backend

3. docker-compose up -d 
   Note: This will start two services. App and db. App connect to MySQL DB for data storing and retrieving. 

4. Use Postman to connect to API and test the code.

## How to contribute to backend code and deliver *without* Docker
(Note this may create buil environment conflicts with development setup. Suggest to user docker)

1. Fork the repo https://github.com/shivakrishnaamandu/VoterCRM_Backend.git     
   Note: Forking is different than cloning. Check online tutors for more details. 

2. Clone your repo and change working directory to VoterCRM_Backend.

3. Install the required packages from requirements.txt
   
   pip install -r BackEnd/requirements.txt

4. You can make changes in the backend code and build locally and test with docker compose. 
   Or
   You can just use your favaourite IDE to run the main.py

5. Commit the changes after testing locally. And contribute back to parent branch.

## How to contribute to backend code and deliver with Docker
1. Fork the repo https://github.com/shivakrishnaamandu/VoterCRM_Backend.git
   Note: Forking is different than cloning. Check online tutors for more details. 

2. Clone your repo and change working directory to VoterCRM_Backend.

3. open docker-compose.yml and enable 'volumes:' under app service. Check for the comment. 

4. run 'docker compose up -d' , this will mount your local folder BackEnd in container.
5. Make changes in BackEnd folder and just re run 'docker compose -d'. This will reflect local changes in container.
6. Commit the changes done in 'BackEnd' folder and push it to remote main branch. 

5. Commit the changes after testing locally. And contribute back to parent branch.
