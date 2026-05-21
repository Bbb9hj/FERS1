import os
from flask import Flask, render_template_string

# إعداد تطبيق Flask
app = Flask(__name__)

@app.route('/')
def home():
    """
    قراءة ملف الفهرس الشامل (index.html) مباشرة من المجلد الرئيسي
    وتقديمه مباشرة كصفحة ويب تفاعلية فائقة السرعة.
    """
    try:
        with open('index.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        return render_template_string(html_content)
    except FileNotFoundError:
        return "خطأ: لم يتم العثور على ملف index.html في المجلد الرئيسي لخدمتكم.", 404

if __name__ == '__main__':
    # الحصول على المنفذ الافتراضي الموفر تلقائياً من الاستضافة (مثل Render)
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)