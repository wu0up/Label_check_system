from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django import template
from datetime import datetime
from django.views.generic import TemplateView
from SQLextract import extrac_QA_label, update_sql
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import pandas as pd
# from .models import Post # 匯入需要的model

# Create your views here.
# 使用者填單的頁面
def check(request):
    predict_label=request.GET.get('label', '')
    utrac_id=request.GET.get('utrac_id', '')
    # 如果params沒有資料，就不顯示
    # 如果bks沒有資料，就不顯示
    params = extrac_QA_label(predict_label, 'fac_para')
    bks = extrac_QA_label(predict_label, 'usual_para')
    print(predict_label)
    print(utrac_id)
    label_df = pd.read_excel('類別標籤清單.xlsx')
    label_dict=label_df.set_index('分類').T.to_dict()
    print(label_dict)
    label ={'name':str(predict_label), 'description':label_dict.get(predict_label)['說明']}
    local_dic = locals()
    return render_to_response('check_predict_label.html',locals()) #要把predict_label和utrac_id傳到checked

@csrf_exempt
def checked(request):
    if request.method=='POST':
        # print(request.POST)
        # 將表單1的資料拿過來
        params_check=request.POST['params_check']
        bk_check = request.POST['bk_check']
        label_check_yes=request.POST['yes_no']
        utrac_id = request.POST['utrac_id']
        # label_check_no=request.POST['no']
        # print(params_check)
        # print(bk_check)
        # print(label_check_yes)
        # print(label_check_no)
        if len(params_check) ==0 and len(bk_check) ==0:
            update_sql(int(utrac_id), 2)
        elif (len(params_check)!=0 or len(bk_check)!=0) and label_check_yes==0:
             update_sql(int(utrac_id), 2)
        else:
            update_sql(int(utrac_id), 1)
        return render_to_response('index.html')
    #     #確認表單2有資料
    #     #將此
    else:
        return render_to_response('index.html')
    #     mess='表單資料尚未送出'
    # return render(request, 'index.html', {
    #     'current_time': str(datetime.now()),
    # })
    # return render_to_response('index.html')  #這邊可以放入utrac id




