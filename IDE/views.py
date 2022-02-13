
from django.shortcuts import render
import subprocess
from .ocr import ocr_core
import os
from django.core.files.storage import FileSystemStorage
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


dir = str(os.getcwd()).replace('\\','/')
def IDE(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        try:
            code = request.POST.get('code')
        except:
            pass
        file = request.POST.get('myfile')
        try:
            if request.FILES['myfile']:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage(location='media/')
                filename = fs.save(myfile.name, myfile)
                code = ocr_core(os.path.join(BASE_DIR, 'media/')+filename)
        except:
            pass

        if type == 'python':
            file = open('code.py','w')
            file.write(code)
            file.close()
            output = subprocess.run(['python', '-c', 'code.py'],capture_output=True)
            exit_code = output.returncode
            error = output.stderr
            result = output.stdout
        elif type == 'cpp':
            file = open('code.cpp','w')
            file.write(code)
            file.close()
            output = subprocess.run(['g++',dir+'/code.cpp', '-o', 'output'], input=code.encode(), capture_output=True)
            output = subprocess.run(dir+'/output', input=code.encode(), capture_output=True)
            exit_code = output.returncode
            error = output.stderr
            result = output.stdout
        elif type == 'c':
            file = open('code.c','w')
            file.write(code)
            file.close()
            output = subprocess.run(['gcc',dir+'/code.c', '-o', 'output'], input=code.encode(), capture_output=True)
            output = subprocess.run(dir+'/output', input=code.encode(), capture_output=True)
            exit_code = output.returncode
            error = output.stderr
            result = output.stdout
        elif type == 'java':
            file = open('code.java','w')
            file.write(code)
            file.close()
            output = subprocess.run(['javac',dir+'/code.java'], input=code.encode(), capture_output=True)
            output = subprocess.run(['java', 'code'], input=code.encode(), capture_output=True)
            exit_code = output.returncode
            error = output.stderr
            result = output.stdout
        elif type == 'javascript':
            file = open('code.js','w')
            file.write(code)
            file.close()
            output = subprocess.run(['node', 'code.js'], input=code.encode(), capture_output=True)
            exit_code = output.returncode
            error = output.stderr
            result = output.stdout
        else:
            exit_code = 0
            error = ''
            result = ''
        data = {
            'code' : code,
            'exit_code': str(exit_code),
            'error': error.decode("utf-8") ,
            'result': str(result.decode("utf-8") )
        }

        return render(request,'index.html',context=data)
    return render(request,'index.html')


def blog(request):
    return render(request,'blog.html')

def new_blog(request):
    return render(request,'new_blog.html')

def opportunity(request):
    return render(request,'opportunity.html')

def tutorial(request):
    return render(request,'tutorials.html')