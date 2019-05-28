import os
from flask import Flask,redirect
import sys
import urllib.request

version = os.environ['version']
app = Flask(__name__)

@app.route('/latest/online-win/')
def winonline(version):
    target_url = "https://vscjavaci.blob.core.windows.net/vscodejavainstaller/latest/VSCodeJavaInstaller-online-win-%s.exe"%version
    return target_url
    #return redirect(target_url, code=302)

@app.route('/latest/win-x64-jdk8/')
def jdk8winx64(version):
    target_url = "https://vscjavaci.blob.core.windows.net/vscodejavainstaller/latest/VSCodeJava8Installer-win-x64-%s.exe"%version
    return redirect(target_url, code=302)

@app.route('/latest/win-x64-jdk11/')
def jdk11winx64(version):
    target_url = "https://vscjavaci.blob.core.windows.net/vscodejavainstaller/latest/VSCodeJava11Installer-win-x64-%s.exe"%version
    return redirect(target_url, code=302)

@app.route('/latest/win-x64-jdk12/')
def jdk12winx64(version):
    target_url = "https://vscjavaci.blob.core.windows.net/vscodejavainstaller/latest/VSCodeJava12Installer-win-x64-%s.exe"%version
    return redirect(target_url, code=302)

@app.route('/latest/win-x86-jdk8/')
def jdk8winx86(version):
    target_url = "https://vscjavaci.blob.core.windows.net/vscodejavainstaller/latest/VSCodeJava8Installer-win-x86-%s.exe"%version
    return redirect(target_url, code=302)

@app.route('/latest/win-x86-jdk11/')
def jdk11winx86(version):
    target_url = "https://vscjavaci.blob.core.windows.net/vscodejavainstaller/latest/VSCodeJava11Installer-win-x86-%s.exe"%version
    return redirect(target_url, code=302)

@app.route('/latest/win-x86-jdk12/')
def jdk12winx86(version):
    target_url = "https://vscjavaci.blob.core.windows.net/vscodejavainstaller/latest/VSCodeJava12Installer-win-x86-%s.exe"%version
    return redirect(target_url, code=302)
