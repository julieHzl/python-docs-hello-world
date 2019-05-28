import os
from flask import Flask,redirect
import sys

version = "0.1.0"
app = Flask(__name__)

@app.route('/latest/online-win/')
def wiononline():
    target_url = "https://vscjavaci.blob.core.windows.net/vscodejavainstaller/latest/VSCodeJavaInstaller-online-win-%s.exe"%version
    return redirect(target_url, code=302)

@app.route('/latest/win-x64-jdk8/')
def jdk8winx64():
    target_url = "https://vscjavaci.blob.core.windows.net/vscodejavainstaller/latest/VSCodeJava8Installer-win-x64-%s.exe"%version
    return redirect(target_url, code=302)

@app.route('/latest/win-x64-jdk11/')
def jdk11winx64():
    target_url = "https://vscjavaci.blob.core.windows.net/vscodejavainstaller/latest/VSCodeJava11Installer-win-x64-%s.exe"%version
    return redirect(target_url, code=302)

@app.route('/latest/win-x64-jdk12/')
def jdk12winx64():
    target_url = "https://vscjavaci.blob.core.windows.net/vscodejavainstaller/latest/VSCodeJava12Installer-win-x64-%s.exe"%version
    return redirect(target_url, code=302)

@app.route('/latest/win-x86-jdk8/')
def jdk8winx86():
    target_url = "https://vscjavaci.blob.core.windows.net/vscodejavainstaller/latest/VSCodeJava8Installer-win-x86-%s.exe"%version
    return redirect(target_url, code=302)

@app.route('/latest/win-x86-jdk11/')
def jdk11winx86():
    target_url = "https://vscjavaci.blob.core.windows.net/vscodejavainstaller/latest/VSCodeJava11Installer-win-x86-%s.exe"%version
    return redirect(target_url, code=302)

@app.route('/latest/win-x86-jdk12/')
def jdk12winx86():
    target_url = "https://vscjavaci.blob.core.windows.net/vscodejavainstaller/latest/VSCodeJava12Installer-win-x86-%s.exe"%version
    return redirect(target_url, code=302)
