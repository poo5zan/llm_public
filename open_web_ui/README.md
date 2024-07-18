## Deploy Open Web UI with Ollama in Free Tier of Google Colab and access the web application via public url using ngrok

This document demonstrates deploying open web UI in Free Tier of Google Colab. "Open WebUI is an extensible, feature-rich, and user-friendly self-hosted WebUI designed to operate entirely offline. It supports various LLM runners, including Ollama and OpenAI-compatible APIs". More information can be found in it's official page: https://docs.openwebui.com/. 

The app hosted in Free Tier of Google Colab can be used for around 1 to 2 hours a day with one gmail account. It's highly recommended to use GPU to speed-up the performance. 

### Technologies
1. Ollama (https://ollama.com/)
2. Open WebUI (https://docs.openwebui.com/)
3. Ngrok (https://ngrok.com/)
4. Google Colab (https://colab.research.google.com/)

### How to
1. Open the notebook(https://github.com/poo5zan/llm_public/blob/main/open_web_ui/open_web_ui.ipynb) in google colab by clicking on 'Open in Colab' in the specified file.
2. Connect to the GPU runtime by clicking on 'Connect' button. 
3. Validate that the connected rumtime has GPU. The resource tab should show RAM, GPU and Harddisk available. If you can't see the GPU, then change the runtime by clicking on 'Runtime -> Change runtime type -> Select 'T4 GPU' -> Save


<img src="https://github.com/poo5zan/llm_public/blob/main/open_web_ui/images/resource_utilization.png" width="500" height="400" />

4. Run the cell to install Ollama and pull models.
5. Generate a public url with ngrok. You will need to create an account in ngrok if you don't have one. Then, go to https://dashboard.ngrok.com/get-started/your-authtoken and copy your personal access token. In the code "!ngrok config add-authtoken {your-personal-token}", replace {your-personal-token} with the copied token. 
6. In my experiment, the public url was https://4d0c-34-168-85-99.ngrok-free.app . <b style="color:red">On each run, the public url will be different.</b> Click the public url link. It should show something like following:


<img src="https://github.com/poo5zan/llm_public/blob/main/open_web_ui/images/ngrok_initial.png" width="800" height="400" />

Since, we haven't started our webUI service yet. The red mark is valid.

7. Start Open Web UI. It will take some time around 5-8 minutes to download all the dependencies. Wait until you see log message saying 'Uvicorn running on http://0.0.0.0:8081 as shown in screenshot below:


<img src="https://github.com/poo5zan/llm_public/blob/main/open_web_ui/images/open_web_ui_started.png" width="600" height="400" />


8. Access previous public url, you should now see a login page. Create a new account, then start using the app.


<img src="https://github.com/poo5zan/llm_public/blob/main/open_web_ui/images/open_web_ui_signin.png" width="600" height="400" />


 <b style="color:green">
If you are happy with your experiments and need me for further information like hosting it in a production environment, then contact me on my linkedIn https://www.linkedin.com/in/pujan-mhjn/
</b>


