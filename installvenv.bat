@echo off
if not exist Lib (
	virtualenv .
	scripts\activate
	pip install -r requirements.txt
) else (
	echo Already installed.
)