import os
from flask import Flask, render_template

app = Flask(__name__)

# --- قاعدة البيانات الكاملة للروابط (14 رابط) ---
import os
from flask import Flask, render_template

app = Flask(__name__)

import os
from flask import Flask, render_template

app = Flask(__name__)

LINKS = {
    # الرابط الجديد للكاتب (يمكن تحديثه من الموقع)
    "clerk_request": "https://unrwaorg.sharepoint.com/", 
    
    # الروابط الأسبوعية
    "load_time": "https://unrwaorg-my.sharepoint.com/:x:/r/personal/n_alnashash_unrwa_org/_layouts/15/Doc.aspx?sourcedoc=%7BE3DE7CA0-279B-48C8-8887-23DC3AE346AF%7D&file=Copy%20of%20Load%20Work%20Time%20for%20Zarka%20DRs%20-%202022.xlsx&wdLOR=c1D546678-86BC-42C8-8810-4059AC58C5FE&fromShare=true&action=default&mobileredirect=true",
    "encd": "https://unrwaorg-my.sharepoint.com/:x:/r/personal/n_alnashash_unrwa_org/_layouts/15/Doc.aspx?sourcedoc=%7B36B826FC-7710-4FE2-AA08-D5B8520F50DD%7D&file=Copy%20of%20Copy%20of%20NCD%20application-%20Zarka%20Area%20-%20Copy.xlsx&wdLOR=cA8C5456A-DD17-4DD2-9F9E-370521C97FDF&fromShare=true&action=default&mobileredirect=true",
    "emch": "https://unrwaorg-my.sharepoint.com/:x:/r/personal/n_alnashash_unrwa_org/_layouts/15/Doc.aspx?sourcedoc=%7B0EB8E0DC-A41C-4880-A966-625DDFE550B4%7D&file=Copy%20of%20Copy%20of%20MCH%20%20application-%20Zarka%20Area.xlsx&wdLOR=c9B8AD8B6-CEB6-428B-B793-D0561D4DA777&fromShare=true&action=default&mobileredirect=true",
    
    # البدلاء والشؤون الإدارية
    "timesheet": "https://unrwaorg-my.sharepoint.com/:x:/r/personal/n_alnashash_unrwa_org/_layouts/15/Doc.aspx?sourcedoc=%7B14B58B1C-7889-482D-B15C-FD10A92E11F4%7D&file=Health%20DP%20staff%20Timesheet.xlsx&fromShare=true&action=default&mobileredirect=true",
    "contracts": "https://unrwaorg.sharepoint.com/sites/ZarkaArea/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FZarkaArea%2FShared%20Documents%2F%D8%B9%D9%82%D9%88%D8%AF%20%D8%A7%D9%84%D9%85%D9%88%D8%B8%D9%81%D9%8A%D9%86%20%D8%A7%D9%84%D8%A8%D8%AF%D9%84%D8%A7%D8%A1&viewid=67d54a97%2Dc601%2D4fe8%2D8510%2D641a56daee60",
    "performance_2026": "https://unrwaorg.sharepoint.com/:f:/r/sites/ZarkaArea/Shared%20Documents/%D8%AA%D9%82%D9%8A%D9%8A%D9%85%20%D8%A3%D8%AF%D8%A7%D8%A1%20%D8%A7%D9%84%D9%85%D9%88%D8%B8%D9%81%D9%8A%D9%86%20%D8%A7%D9%84%D8%A8%D8%AF%D9%84%D8%A7%D8%A1%202026?csf=1&web=1&e=r4F0RK",
    "documents": "https://unrwaorg.sharepoint.com/:f:/r/sites/ZarkaArea/Shared%20Documents/%D9%88%D8%AB%D8%A7%D8%A6%D9%82%20%D8%A7%D9%84%D9%85%D9%88%D8%B8%D9%81%D9%8A%D9%86%20%D8%A7%D9%84%D8%A8%D8%AF%D9%84%D8%A7%D8%A1?csf=1&web=1&e=bsj8nX",
    "replacement_data": "https://unrwaorg-my.sharepoint.com/:x:/r/personal/n_alnashash_unrwa_org/_layouts/15/Doc.aspx?sourcedoc=%7BF8D49114-2D59-45F1-BFC4-28131329E5FE%7D&file=بيانات%20الموظفين%20البدلاء.xlsx&fromShare=true&action=default&mobileredirect=true",
    "requests": "https://unrwaorg-my.sharepoint.com/:x:/r/personal/n_alnashash_unrwa_org/_layouts/15/Doc.aspx?sourcedoc=%7B8F51B034-6A3E-479E-B72A-2BD2A24E75E1%7D&file=REQUEST%20FORM_JFO_Temp%20Replacement.xlsx&fromShare=true&action=default&mobileredirect=true",
    
    # مستندات عامة وإحصائيات
    "manning": "https://unrwaorg-my.sharepoint.com/:x:/r/personal/n_alnashash_unrwa_org/_layouts/15/Doc.aspx?sourcedoc=%7B1348D2C9-BB99-4CD0-8F41-48788004CDC2%7D&file=Manning%20Table%20%20%20%20Health%20%20%20Zarka%20%20%2019.03.2025.xlsx&wdLOR=cEE240FC3-1BFE-4864-9D80-F863855BDE30&fromShare=true&action=default&mobileredirect=true",
    "daily_paid": "https://unrwaorg-my.sharepoint.com/:x:/r/personal/n_alnashash_unrwa_org/_layouts/15/Doc.aspx?sourcedoc=%7BA8136684-5D00-41EF-A450-C9F8627DB25F%7D&file=All%20DP%20-%20Health%20-%20Zarka_.xlsx&wdLOR=c17AB2563-A195-4392-8180-9005FA4001E2&fromShare=true&action=default&mobileredirect=true",
    "other_docs": "https://unrwaorg.sharepoint.com/:f:/r/sites/ZarkaArea/Shared%20Documents/%D9%88%D8%AB%D8%A7%D8%A6%D9%82%20%D8%A3%D8%AE%D8%B1%D9%89%20%D8%AA%D8%B7%D9%84%D8%A8%20%D9%85%D9%86%20%D8%A7%D9%84%D8%B9%D9%8A%D8%A7%D8%AF%D8%A7%D8%AA-%20%D8%B9%D9%86%D8%AF%20%D8%A7%D9%84%D8%B7%D9%84%D8%A8-?csf=1&web=1&e=WKxAPH",
    "forms": "https://unrwaorg.sharepoint.com/:f:/r/sites/ZarkaArea/Shared%20Documents/%D9%86%D9%85%D8%A7%D8%B0%D8%AC?csf=1&web=1&e=zjS2po",
    "clients": "https://unrwaorg-my.sharepoint.com/:x:/r/personal/n_alnashash_unrwa_org/_layouts/15/Doc.aspx?sourcedoc=%7B40A0F467-2401-49C1-9B74-4C248460075C%7D&file=Distribution_of_Clients.xlsx&fromShare=true&action=default&mobileredirect=true"
}

@app.route('/')
def home():
    return render_template('index.html', links=LINKS)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
