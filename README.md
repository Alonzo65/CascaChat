# CascaChat

<h2>#Functionality:</h2>

This project showcases a Chat bot that will interact with the user and teach them about a certain subject. The chat bot communicates using audio clips and getting input through voice clips from the user. The front-end was created using React and backend was made with python.

<h2>#Technologies/Frameworks/Languages Used:</h2>

 -React framework was used for the Frontend

  -Python for the backend

  -Frontend: Node js, yarn, ts-node

-Main packages used for backend: FastAPI, OpenAI, Eleven labs

-Main packages used for frontend: tailwindcss, yarn, vite


<h2>#Setup:</h2>

- <b>Installations:</b>
  - Go into the backend directory and into the .env file, here you will need to populate the variables OPEN_AI_ORG and OPEN_AI_KEY with your openai keys/secrets, as well as ELEVEN_LABS_API_KEY variable with your eleven labs key from your account.
  - First make sure you have Python 3.10 installed as well as Node.js.
  - Then you will open up a terminal and go into the backend directory of the CascaChat directory, here you will create a virtual environment that uses python 3.10. To do this you will type in to the terminal _python3.10 -m venv venv_ and press enter, this will create a venv directory. From here you will need to activate the virtual environment by either entering in _venv\Scripts\activate_ from the backend directory, or traverse into the Scripts directory and enter in _activate_ into the terminal and press enter. Once activated, traverse back to the parent directory CascaChat in the terminal.
  - Then in the terminal you will do _npm install --global yarn_ to get the latest version of yarn. Next, you will enter _npm i ts-node@10.9.1_ or a later version and press enter.
  - Make sure to install all the packages from requirements.txt as well by doing _pip install -r requirements.txt_ in the terminal. Also make sure to install uvicorn by typing _pip install uvicorn[standard]_ into the terminal and press enter, if you encounter any issues go to uvicorn website to troubleshoot [here](https://www.uvicorn.org/). Then change directory into frontend and type _yarn --exact_ into the terminal to install all dependencies.

- <b>Steps:</b>
  - Step 1: You will need two open terminals in the CascaChat directory(this can easily be done in VS Code).
  - Step 2: In one of the terminals you will change directory into the backend directory and you will then type _python -m uvicorn main:app --reload_ into the terminal and press enter, if that doesnt work try _uvicorn main:app --reload_ instead. You should see a message saying Application startup complete.
  - Step 3: Then in the other terminal you will change directory into the frontend directory and type in _yarn dev_ and press enter, then it will provide a local host link, copy it and paste it into your browser. This should display the dashboard for CascaChat.
  - Step 4: Now you are ready to begin interacting with Casca.

