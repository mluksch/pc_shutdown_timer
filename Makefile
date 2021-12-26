build: config.py main.py timer.py gui.py utils.py
	pyinstaller --onefile --icon=shutdown.ico --noconsole --path=venv/Lib/site-packages --name=Shutdown main.py