build: config.py main.pyw timer.py gui.py utils.py
	pyinstaller --onefile --icon=shutdown.ico --path=venv/Lib/site-packages --name=Shutdown main.pyw