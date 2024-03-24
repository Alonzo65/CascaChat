# CascaChat

#Functionality

this project showcases a Chat bot that will interact with the user and teach them about a certain subject. the chat bot communicates using audio clips and getting input through voice clips from the user. the front-end was created using React and OpenAi, and backend was made with python.

#Technologies/Frameworks/Languages Used:

-React framework was used for the Frontend

-Python for the backend

-Frontend: Node js, yarn, ts-node

-Packages for python/backend: FastAPI, OpenAI,

-Packages for frontend(double check these): tailwindcss, yarn, vite


#Setup:

-First make sure you have the latest version of Python installed as well as Node.js. Then in a terminal you will do _npm install --global yarn_ to get the latest version of yarn. Next, you will enter _npm i ts-node@10.9.1_ or a later version and press enter.

-Make sure to install all the packages from requirements.txt first. Then change directory into frontend and type _yarn --exact_ into the terminal to install all dependencies.
-Step 1: You will need two open terminals in the CascaChat directory(this can be easily done in VS Code).

-Step 2: In one of the terminals you will change directory into the backend directory and type _venv/Scripts/activate_ into the console and press enter. Then once you are in the virtual environment, you will then type _uvicorn main:app --reload_ into the terminal and press enter. You should see a message saying Application startup complete.

-Step 3: In one of the terminals you will change directory into the frontend directory and type in _yarn dev_ and press enter, then it will provide a local host link, copy it and paste it into your browser. This should display the dashboard for CascaChat.

-Step 4: Now you are ready to begin interacting with Casca.

