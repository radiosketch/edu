call shell
echo Installing jupyter_http_over_ws
call pip install jupyter_http_over_ws
call jupyter serverextension enable --py jupyter_http_over_ws
echo Starting the Juputer Notebook in a new cmd
call start cmd /k jupyter notebook --no-browser --NotebookApp.allow_origin="https://colab.research.google.com" --port=8888 --NotebookApp.port_retries=0
echo.
echo 1. Copy the initial backend URL
echo 2. In Colaboratory, click the "Connect" button and select "Connect to local runtime...". Enter the URL from the previous step in the dialog that appears and click the "Connect" button. After this, you should now be connected to your local runtime.
