build: config.py main.py timer.py gui.py utils.py
	pipenv install filelock && pyinstaller --onefile --icon=shutdown.ico --noconsole --path=venv/Lib/site-packages --name=Shutdown main.py