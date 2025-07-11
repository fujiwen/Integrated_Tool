import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys
import subprocess
from datetime import datetime

def get_config_path():
    """获取配置文件路径"""
    if getattr(sys, 'frozen', False):
        # 如果是打包后的exe运行
        base_path = os.path.dirname(sys.executable)
    else:
        # 如果是脚本运行
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, 'config.txt')

def ensure_config_file():
    """确保配置文件存在，如果不存在则创建"""
    config_path = get_config_path()
    if not os.path.exists(config_path):
        default_config = '''B2:海口索菲特大酒店
D2:海南省海口市龙华区滨海大道105号
E2:符小瑜 0898-31289999
B32:abbyfu@hksft.com
hotelname:海口索菲特大酒店
Sheet_tittle:供货明细表'''
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(default_config)
        return True
    return False

class IntegratedTool:
    def __init__(self, root):
        self.root = root
        
        # 首先检查过期时间
        check_expiration_time()
        
        self.root.title("供应商对账工具集")
        
        # 设置窗口大小并居中
        self.set_window_geometry(400, 400)
        
        # 创建主框架
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建标题标签
        title_label = ttk.Label(self.main_frame, text="请选择要使用的功能：", font=("微软雅黑", 12))
        title_label.pack(pady=20)
        
        # 创建按钮框架
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)
        
        # 创建供应商供货明细表工具按钮
        self.recon_btn = ttk.Button(
            button_frame,
            text="供应商供货明细表工具",
            command=self.launch_recon_tool,
            width=25
        )
        self.recon_btn.pack(pady=10)
        
        # 创建供应商对帐确认函按钮
        self.classification_btn = ttk.Button(
            button_frame,
            text="供应商对帐确认函",
            command=self.launch_classification_tool,
            width=25
        )
        self.classification_btn.pack(pady=10)
        
        # 添加开发者信息
        self.dev_label = ttk.Label(self.main_frame, text="Powered By Cayman Fu @ Sofitel HAIKOU 2025 Ver 2.3")
        self.dev_label.pack(side=tk.BOTTOM, pady=10)
    
    def set_window_geometry(self, width, height):
        """设置窗口大小并居中"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def launch_recon_tool(self):
        """启动供应商供货明细表工具"""
        script_path = os.path.join(os.path.dirname(__file__), "Bldbuy_Recon_UI.py")
        try:
            if sys.platform == "win32":
                subprocess.Popen([sys.executable, script_path])
            else:  # macOS 和 Linux
                subprocess.Popen([sys.executable, script_path])
        except Exception as e:
            messagebox.showerror("错误", f"启动供应商供货明细表工具失败：\n{str(e)}")
    
    def launch_classification_tool(self):
        """启动供应商对帐确认函"""
        script_path = os.path.join(os.path.dirname(__file__), "Product_Classification_Tool.py")
        try:
            if sys.platform == "win32":
                subprocess.Popen([sys.executable, script_path])
            else:  # macOS 和 Linux
                subprocess.Popen([sys.executable, script_path])
        except Exception as e:
            messagebox.showerror("错误", f"启动供应商对帐确认函失败：\n{str(e)}")
    
def check_expiration_time():
    """检查时间是否到期"""
    current_date = datetime.now()
    expiration_date = datetime(2025, 12, 31)  # 2025年底到期
    
    if current_date > expiration_date:
        messagebox.showerror("错误", "DLL注册失败，请联系Cayman更新")
        sys.exit(1)

if __name__ == "__main__":
    # 首先检查过期时间
    check_expiration_time()
    
    # 检查并确保配置文件存在
    if ensure_config_file():
        messagebox.showinfo("提示", "已创建默认配置文件：config.txt")
    
    root = tk.Tk()
    app = IntegratedTool(root)
    root.mainloop()