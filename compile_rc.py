import os
import subprocess

def compile_rc():
    try:
        # 检查图标文件是否存在
        icon_file = 'favicon.ico'
        if not os.path.exists(icon_file):
            print(f'Error: Icon file {icon_file} not found')
            return False

        # 检查 .rc 文件是否存在
        rc_file = 'app.rc'
        if not os.path.exists(rc_file):
            print(f'Error: Resource file {rc_file} not found')
            return False

        # 检查是否安装了 windres
        try:
            subprocess.run(['windres', '--version'], check=True, capture_output=True, encoding='utf-8')
        except subprocess.CalledProcessError:
            print('Error: windres not found. Please install MinGW-w64 toolchain')
            return False
        
        # 编译 .rc 文件
        try:
            subprocess.run(['windres', rc_file, '-O', 'coff', '-o', 'app.res'], 
                         check=True, encoding='utf-8', errors='replace')
            print('Resource file compiled successfully')
            return True
        except subprocess.CalledProcessError as e:
            print(f'Error compiling resource file: {str(e)}')
            return False
    except Exception as e:
        print(f'Error: {str(e)}')
        return False

if __name__ == '__main__':
    compile_rc()