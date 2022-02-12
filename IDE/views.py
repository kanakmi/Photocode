from imp import cache_from_source
from django.shortcuts import render
import subprocess
from django.http import HttpResponse, JsonResponse
# Create your views here.
import io
import os
dir = str(os.getcwd()).replace('\\','/')
def IDE(request):
    type = 'c++'
    code = """
        #include <stdio.h>
        int main(){
            printf("Hello World");
            return 0;
        }
    """
    if type == 'python':
        file = open('code.py','w')
        file.write(code)
        file.close()
        output = subprocess.run(['python', '-c', 'code.py'],capture_output=True)
        exit_code = output.returncode
        error = output.stderr
        result = output.stdout
    if type == 'c++':
        file = open('code.cpp','w')
        file.write(code)
        file.close()
        output = subprocess.run(['g++',dir+'/code.cpp', '-o', 'output'], input=code.encode(), capture_output=True)
        output = subprocess.run(dir+'/output', input=code.encode(), capture_output=True)
        exit_code = output.returncode
        error = output.stderr
        result = output.stdout
    if type == 'c':
        file = open('code.c','w')
        file.write(code)
        file.close()
        output = subprocess.run(['gcc',dir+'/code.c', '-o', 'output'], input=code.encode(), capture_output=True)
        output = subprocess.run(dir+'/output', input=code.encode(), capture_output=True)
        exit_code = output.returncode
        error = output.stderr
        result = output.stdout
    if type == 'java':
        file = open('code.java','w')
        file.write(code)
        file.close()
        output = subprocess.run(['javac',dir+'/code.java'], input=code.encode(), capture_output=True)
        output = subprocess.run(['java', 'code'], input=code.encode(), capture_output=True)
        exit_code = output.returncode
        error = output.stderr
        result = output.stdout
    if type == 'javascript':
        file = open('code.js','w')
        file.write(code)
        file.close()
        output = subprocess.run(['node', 'code.js'], input=code.encode(), capture_output=True)
        exit_code = output.returncode
        error = output.stderr
        result = output.stdout

    data = {
        'exit-code': exit_code,
        'error': error,
        'result': result
    }
    return render(request,'index.html')